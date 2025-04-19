from django.urls import path
from . import views

app_name = "food_delivery"  # Namespace for reverse URL resolution

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('restaurants/', views.restaurant_list, name='restaurant_list'),  # List of restaurants
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),  # Restaurant detail and menu

    path('cart/', views.cart, name='cart'),  # View cart
    path('update-cart/', views.update_cart_item, name='update_cart_item'),  # Update cart items (AJAX for menu page)
    path('cart/update/', views.update_cart_item, name='update_cart_item'),  # Update cart items (form from cart.html)
    path('checkout/', views.checkout, name='checkout'),  # Place order
    path('orders/<uuid:pk>/', views.order_detail, name='order_detail'),  # Order detail
    path('orders/<uuid:pk>/update/', views.update_order_status, name='update_order_status'),  # Update order status (manager)

    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('profile/', views.profile, name='profile'),  # Profile update

    path('dashboard/', views.restaurant_dashboard, name='restaurant_dashboard'),  # Manager dashboard
]
