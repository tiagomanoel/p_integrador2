# Import necessary modules and settings from Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [
    # Include the URL patterns from the 'price' app
    path('', include('price.urls')),
    
    # URL pattern for the Django admin site
    path('admin/', admin.site.urls),
]

# Serve media files during development when DEBUG is True
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,  # The URL that handles the media files
        document_root=settings.MEDIA_ROOT  # The filesystem path to the media files
    )
