from django.contrib import admin  # Import the Django admin interface
from django.urls import path, include  # Import functions to define URL patterns
from django.conf import settings  # Import project settings
from django.conf.urls.static import static  # Import helper for serving static/media files in development

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the Django admin panel
    path('', include('food_delivery.urls')),  # Include URL patterns from the 'food_delivery' app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve uploaded media files in development

# Serve media files from MEDIA_URL when in DEBUG mode (for development only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
