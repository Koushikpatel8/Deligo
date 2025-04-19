# forms.py

from django import forms  # Django's form system
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Built-in forms for user creation and login
from django.core.exceptions import ValidationError  # For raising validation errors
from django.utils.translation import gettext_lazy as _  # For internationalization and translatable text
from .models import *  # Import all models from the current app

# -------------------------------
# Registration Form for Customers
# -------------------------------
class RegistrationForm(UserCreationForm):
    # Additional fields added to the default UserCreationForm
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        help_text="Format: +1234567890"
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=True
    )

    class Meta:
        model = User  # Use the custom User model
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']

    def clean_phone(self):
        # Ensure the phone number starts with a country code
        phone = self.cleaned_data.get('phone')
        if not phone.startswith('+'):
            raise ValidationError("Phone number must start with country code (e.g., +1)")
        return phone

    def save(self, commit=True):
        # Save the user instance with the CUSTOMER role
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.type = User.Types.CUSTOMER  # Explicitly set the user type
        if commit:
            user.save()
        return user

# -------------------------------
# Login Form
# -------------------------------
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username or Email"),
        widget=forms.TextInput(attrs={'autofocus': True})
    )

# -------------------------------
# Profile Update Form
# -------------------------------
class ProfileForm(forms.ModelForm):
    # Fields for updating additional customer profile data
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        # Pre-fill form fields with existing customer profile data
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'customerprofile'):
            self.fields['phone'].initial = self.instance.customerprofile.phone
            self.fields['address'].initial = self.instance.customerprofile.address

    def save(self, commit=True):
        # Save user and customer profile data
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = user.customerprofile
            profile.phone = self.cleaned_data['phone']
            profile.address = self.cleaned_data['address']
            profile.save()
        return user

# -------------------------------
# Restaurant Form for Managers
# -------------------------------
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'contact_number', 'opening_hours', 'image']
        widgets = {
            'opening_hours': forms.TextInput(attrs={'placeholder': 'e.g., 9:00 AM - 10:00 PM'}),
        }

# -------------------------------
# Menu Category Form
# -------------------------------
class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = ['name', 'description', 'order']

# -------------------------------
# Menu Item Form
# -------------------------------
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['category', 'name', 'description', 'price', 'image', 'is_available', 'preparation_time']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_price(self):
        # Ensure the price is greater than zero
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Price must be greater than zero")
        return price

# -------------------------------
# Order Status Form (Manager view)
# -------------------------------
class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

    def __init__(self, *args, **kwargs):
        # Dynamically restrict status options based on current order status
        super().__init__(*args, **kwargs)
        current_status = self.instance.status
        if current_status == Order.Status.CONFIRMED:
            self.fields['status'].choices = [
                (Order.Status.CONFIRMED, _('Confirmed')),
                (Order.Status.PREPARING, _('Preparing')),
                (Order.Status.CANCELLED, _('Cancelled'))
            ]
        elif current_status == Order.Status.PREPARING:
            self.fields['status'].choices = [
                (Order.Status.PREPARING, _('Preparing')),
                (Order.Status.READY, _('Ready for Pickup')),
                (Order.Status.CANCELLED, _('Cancelled'))
            ]
        # Additional transitions can be added as needed

# -------------------------------
# Checkout Form
# -------------------------------
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address', 'special_instructions', 'payment_method']
        widgets = {
            'delivery_address': forms.Textarea(attrs={'rows': 3}),
            'special_instructions': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        # Pre-fill delivery address from customer profile if available
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'customerprofile'):
            self.fields['delivery_address'].initial = user.customerprofile.address
