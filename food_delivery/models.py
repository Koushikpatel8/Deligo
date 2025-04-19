# models.py

import uuid  # For generating unique order IDs
from django.db import models  # Django ORM base classes
from django.contrib.auth.models import AbstractUser  # Base class for custom user model
from django.conf import settings  # Access project settings
from django.core.validators import MinValueValidator  # For validating positive price values
from django.utils.translation import gettext_lazy as _  # For internationalization
from django.db.models.signals import post_save  # Signal for post-save event
from django.dispatch import receiver  # Decorator to connect signals

# -------------------------------
# Custom User Model
# -------------------------------
class User(AbstractUser):
    class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        RESTAURANT_MANAGER = "MANAGER", "Restaurant Manager"
        DELIVERY_PERSON = "DELIVERY", "Delivery Person"

    type = models.CharField(max_length=10, choices=Types.choices, default=Types.CUSTOMER)  # User role/type
    phone = models.CharField(max_length=15, blank=True)  # Optional phone field
    email = models.EmailField(_('email address'), unique=True)  # Unique email used for authentication

# -------------------------------
# Customer Profile
# -------------------------------
class CustomerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'type': User.Types.CUSTOMER}  # Ensure only customer-type users get a profile
    )
    address = models.TextField()  # Customer address
    phone= models.CharField(max_length=15, blank=True)

    preferred_payment_method = models.CharField(max_length=50, blank=True)  # Optional field

    def __str__(self):
        return f"{self.user.username}'s Profile"  # Display the profile with username

# -------------------------------
# Restaurant
# -------------------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    opening_hours = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurants/')  # Upload path for restaurant images
    manager = models.OneToOneField(  # Each restaurant has one manager
        User,
        on_delete=models.CASCADE,
        related_name='managed_restaurant'
    )

    def __str__(self):
        return self.name  # Show restaurant name in admin and debug

# -------------------------------
# Menu Category
# -------------------------------
class MenuCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')  # Related to one restaurant
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)  # For ordering categories

    class Meta:
        ordering = ['order']  # Default ordering of categories
        verbose_name_plural = "Menu Categories"  # Admin display name

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"  # Display name with restaurant context

# -------------------------------
# Menu Item
# -------------------------------
class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')  # Belongs to one category
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])  # Price must be >= 0
    image = models.ImageField(upload_to='menu_items/')  # Upload path for item images
    is_available = models.BooleanField(default=True)  # Toggle for availability
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes", default=15)

    def __str__(self):
        return f"{self.name} - {self.category.restaurant.name}"  # Include context of restaurant

# -------------------------------
# Order and Order Item
# -------------------------------
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        CONFIRMED = 'CONFIRMED', _('Confirmed')
        PREPARING = 'PREPARING', _('Preparing')
        READY = 'READY', _('Ready for Pickup')
        ON_THE_WAY = 'ON_THE_WAY', _('On the way')
        DELIVERED = 'DELIVERED', _('Delivered')
        CANCELLED = 'CANCELLED', _('Cancelled')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique order ID
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders',
        limit_choices_to={'type': User.Types.CUSTOMER}
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp at creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp on every update
    delivery_address = models.TextField()
    special_instructions = models.TextField(blank=True)
    payment_method = models.CharField(max_length=50)
    payment_status = models.BooleanField(default=False)

    @property
    def total_price(self):
        # Calculate total price of all items in the order
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Linked to one order
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # Linked to one menu item
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Total price = item price × quantity
    class Meta:
        unique_together = ('order', 'menu_item')
    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

# -------------------------------
# Signal to Create Customer Profile Automatically
# -------------------------------
@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    # Automatically create a CustomerProfile when a new customer user is created
    if created and instance.type == User.Types.CUSTOMER:
        CustomerProfile.objects.create(user=instance)
