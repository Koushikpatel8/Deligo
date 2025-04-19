from django.contrib import admin  # Django admin interface
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # Base admin class for custom user model
from .models import User, CustomerProfile, Restaurant, MenuItem, MenuCategory, Order, OrderItem  # Import all models
from .forms_admin import CustomUserAdminCreationForm  # Custom form for creating users in admin
from django.utils.html import format_html  # For rendering HTML (used in image thumbnail previews)

# -------------------------------
# Custom User Admin
# -------------------------------
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserAdminCreationForm  # Use custom creation form
    model = User  # Link to the custom User model

    # Display these fields in the user list view
    list_display = ('username', 'email', 'type', 'is_staff', 'is_superuser')
    # Enable filtering by user type and permissions
    list_filter = ('type', 'is_staff', 'is_superuser')

    # Extend the default fieldsets to include custom fields
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('type', 'phone')}),
    )
    # Include custom fields in the user creation form
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'phone', 'type')}),
    )

# -------------------------------
# MenuItem Admin with Image Preview
# -------------------------------
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available', 'thumbnail')  # Columns shown in admin list
    list_filter = ('category', 'is_available')  # Enable filtering options
    search_fields = ('name', 'description')  # Enable search functionality
    list_select_related = ('category',)  # Optimize query performance for related fields

    def thumbnail(self, obj):  # Display item image as a small preview
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    thumbnail.short_description = "Image"  # Column header name

# -------------------------------
# Restaurant Admin with Manager Filter
# -------------------------------
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager']  # Columns to show
    search_fields = ['name']  # Allow admin to search restaurants by name

    # Limit manager dropdown to only users with the RESTAURANT_MANAGER role
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "manager":
            kwargs["queryset"] = User.objects.filter(type=User.Types.RESTAURANT_MANAGER)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# -------------------------------
# Order Admin
# -------------------------------
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'restaurant', 'status', 'created_at')  # Columns in list view
    list_filter = ('status', 'created_at', 'restaurant')  # Enable filters by status, time, restaurant
    search_fields = ('id', 'customer__username', 'restaurant__name')  # Search by order ID, customer, or restaurant
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only in the form

# -------------------------------
# Order Item Admin
# -------------------------------
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price')  # List view columns
    list_filter = ('menu_item',)  # Filter by menu item
    search_fields = ('menu_item__name', 'order__id')  # Enable search by item name or order ID

# -------------------------------
# Register All Models
# -------------------------------
admin.site.register(User, UserAdmin)  # Register custom user admin
admin.site.register(CustomerProfile)  # Default admin for profile
admin.site.register(Restaurant, RestaurantAdmin)  # Register with custom restaurant admin
admin.site.register(MenuCategory)  # Default admin
admin.site.register(MenuItem, MenuItemAdmin)  # Register with image preview admin
admin.site.register(Order, OrderAdmin)  # Register order admin
admin.site.register(OrderItem, OrderItemAdmin)  # Register order item admin
