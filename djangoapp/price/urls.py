# Import necessary modules and functions from Django
from django.urls import path
from price.views import index, pji, sobre, pi_db_list
from django.conf.urls.static import static
from django.conf import settings

# Define the app name for namespacing URLs
app_name = 'price'

# URL patterns for the 'price' app
urlpatterns = [
    # Route for the index page
    path('', index, name='index'),
    # Route for the API endpoint that returns currency data
    path('api/', pi_db_list, name='api'),
    # Route for the PJI page
    path('pji/', pji, name='pji'),
    # Route for the About page
    path('sobre/', sobre, name='sobre'),
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
