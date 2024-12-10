# Optimal_Performance_Platform/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.urls_api')),  # Correct module name 'home'
    path('', include('home.urls')),  # Correct module name 'home'
]
