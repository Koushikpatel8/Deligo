import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db import transaction

from .models import User, Restaurant, MenuItem, Order, OrderItem
from .forms import RegistrationForm, LoginForm, ProfileForm, OrderStatusForm

# -----------------------------
# Utility Role Checks
# -----------------------------
def is_customer(user):
    return user.is_authenticated and user.type == User.Types.CUSTOMER

def is_restaurant_manager(user):
    return user.is_authenticated and user.type == User.Types.RESTAURANT_MANAGER

# -----------------------------
# Utility: Cart Count for Navbar
# -----------------------------
def get_cart_count(user):
    if user.is_authenticated:
        cart = Order.objects.filter(customer=user, status=Order.Status.PENDING).first()
        if cart:
            return sum(item.quantity for item in cart.items.all())
    return 0

# -----------------------------
# Public Views
# -----------------------------
def home(request):
    restaurants = Restaurant.objects.all()[:6]
    return render(request, 'food_delivery/home.html', {
        'restaurants': restaurants,
        'cart_count': get_cart_count(request.user)
    })

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'food_delivery/restaurants.html', {
        'restaurants': restaurants,
        'cart_count': get_cart_count(request.user)
    })

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    categories = restaurant.categories.prefetch_related('items')
    return render(request, 'food_delivery/restaurant_detail.html', {
        'restaurant': restaurant,
        'categories': categories,
        'cart_count': get_cart_count(request.user)
    })

# -----------------------------
# Cart and Checkout Logic
# -----------------------------
@login_required
@user_passes_test(is_customer)
def cart(request):
    cart = Order.objects.filter(customer=request.user, status=Order.Status.PENDING).first()
    return render(request, 'food_delivery/cart.html', {
        'cart': cart,
        'cart_count': get_cart_count(request.user)
    })

@csrf_exempt
@login_required
@user_passes_test(is_customer)
@require_http_methods(["POST"])
def update_cart_item(request):
    try:
        data = json.loads(request.body) if request.headers.get('Content-Type') == 'application/json' else request.POST
        menu_item_id = data.get('menu_item_id')
        action = data.get('action')
        quantity = int(data.get('quantity', 1))

        if not menu_item_id or not action:
            return JsonResponse({'success': False, 'error': 'Missing required data'})

        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        restaurant = menu_item.category.restaurant

        # Get cart only if it's for the same restaurant
        cart = Order.objects.filter(
            customer=request.user,
            status=Order.Status.PENDING,
            restaurant=restaurant
        ).first()

        if not cart:
            cart = Order.objects.create(
                customer=request.user,
                status=Order.Status.PENDING,
                delivery_address=request.user.customerprofile.address,
                payment_method='Cash on Delivery',
                restaurant=restaurant
            )

        # Add, update, or remove item
        if action == 'add':
            order_item, created = OrderItem.objects.get_or_create(
                order=cart,
                menu_item=menu_item,
                defaults={'quantity': quantity, 'price': quantity * menu_item.price}
            )
            if not created:
                order_item.quantity += quantity
                order_item.price = order_item.quantity * menu_item.price
                order_item.save()

        elif action == 'update':
            order_item = OrderItem.objects.filter(order=cart, menu_item=menu_item).first()
            if order_item:
                order_item.quantity = quantity
                order_item.price = quantity * menu_item.price
                order_item.save()

        elif action == 'remove':
            OrderItem.objects.filter(order=cart, menu_item=menu_item).delete()

        else:
            return JsonResponse({'success': False, 'error': 'Invalid action'})

        cart_item_count = sum(item.quantity for item in cart.items.all())
        return JsonResponse({'success': True, 'cart_item_count': cart_item_count})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@login_required
@user_passes_test(is_customer)
@require_http_methods(["POST"])
def checkout(request):
    try:
        with transaction.atomic():
            cart = Order.objects.filter(customer=request.user, status=Order.Status.PENDING).first()
            if not cart or not cart.items.exists():
                raise ValueError("Your cart is empty.")

            cart.status = Order.Status.CONFIRMED
            cart.save()
            messages.success(request, "Order placed successfully!")

            return JsonResponse({
                'success': True,
                'redirect_url': reverse('food_delivery:order_detail', kwargs={'pk': cart.pk})
            })

    except Exception as e:
        return JsonResponse({'success': False, 'error': f"Checkout failed: {str(e)}"})

@login_required
@user_passes_test(is_customer)
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, customer=request.user)
    return render(request, 'food_delivery/order_detail.html', {
        'order': order,
        'cart_count': get_cart_count(request.user)
    })

# -----------------------------
# Manager Dashboard + Status Update
# -----------------------------
@login_required
@user_passes_test(is_restaurant_manager)
def restaurant_dashboard(request):
    restaurant = getattr(request.user, 'managed_restaurant', None)

    if not restaurant:
        messages.warning(request, "You are not assigned to any restaurant yet.")
        return redirect('food_delivery:home')

    # Show only non-pending orders
    orders = Order.objects.filter(restaurant=restaurant).exclude(status=Order.Status.PENDING)

    return render(request, 'food_delivery/restaurant_dashboard.html', {
        'restaurant': restaurant,
        'orders': orders,
        'cart_count': get_cart_count(request.user)
    })

@login_required
@user_passes_test(is_restaurant_manager)
def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk, restaurant__manager=request.user)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order status updated successfully.")
            return redirect('food_delivery:restaurant_dashboard')
    else:
        form = OrderStatusForm(instance=order)

    return render(request, 'food_delivery/update_order_status.html', {
        'form': form,
        'order': order,
        'cart_count': get_cart_count(request.user)
    })

# -----------------------------
# Auth and Profile
# -----------------------------
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.type = User.Types.CUSTOMER
            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('food_delivery:home')
    else:
        form = RegistrationForm()

    return render(request, 'food_delivery/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.type == User.Types.RESTAURANT_MANAGER:
                return redirect('food_delivery:restaurant_dashboard')
            return redirect('food_delivery:home')
    else:
        form = LoginForm()

    return render(request, 'food_delivery/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('food_delivery:home')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('food_delivery:profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'food_delivery/profile.html', {
        'form': form,
        'cart_count': get_cart_count(request.user)
    })
