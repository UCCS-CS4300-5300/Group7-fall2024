from django.contrib import admin
from django.urls import path, include
from home import views  # Import the entire views module from home

urlpatterns = [
    path('admin/', admin.site.urls),               # Admin site
    path('api/', include('home.urls_api')),        # Include home app API URLs prefixed with /api/
    path('', include('home.urls')),                # Include home app non-API URLs
]
