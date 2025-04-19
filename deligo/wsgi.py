import os  # Provides functions to interact with the operating system
from django.core.wsgi import get_wsgi_application  # Imports Django’s WSGI application callable

# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deligo.settings')

# Create a WSGI application object that the web server can use to communicate with Django
application = get_wsgi_application()
