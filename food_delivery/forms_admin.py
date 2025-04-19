# food_delivery/forms_admin.py

from django import forms  # Import Django's forms module
from django.contrib.auth.forms import UserCreationForm  # Base form for creating new users
from food_delivery.models import User  # Import the custom User model
from django.core.exceptions import ValidationError  # For raising validation errors

# ------------------------------------------
# Custom User Creation Form for Admin Panel
# ------------------------------------------
class CustomUserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use the custom User model
        fields = ('username', 'email', 'phone', 'type')  # Fields to include in the form

    def clean_email(self):
        """Validate that the email is unique across users."""
        email = self.cleaned_data.get('email')  # Get the email from cleaned form data
        if User.objects.filter(email=email).exists():  # Check if email already exists in DB
            raise ValidationError("A user with this email already exists.")  # Raise error if not unique
        return email  # Return the validated email
