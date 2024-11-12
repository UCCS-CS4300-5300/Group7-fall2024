from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import (
    BuildViewSet, MotherboardViewSet, CPUViewSet, RAMViewSet, StorageViewSet, UserBuildViewSet
)

# Define the router and register the viewsets
router = DefaultRouter()
router.register(r'builds', BuildViewSet)
router.register(r'motherboards', MotherboardViewSet)
router.register(r'cpus', CPUViewSet)
router.register(r'rams', RAMViewSet)
router.register(r'storages', StorageViewSet)

# Define the API urlpatterns
urlpatterns = [
    # Include the router's automatically generated routes
    path('', include(router.urls)),

    # Custom endpoint for fetching builds specific to a user
    path('user_builds/<int:user_id>/', UserBuildViewSet.as_view({'get': 'list'}), name='user_builds'),

    # Custom search endpoints for each component
    path('search/motherboards/', MotherboardViewSet.as_view({'get': 'search'}), name='motherboard_search'),
    path('search/cpus/', CPUViewSet.as_view({'get': 'search'}), name='cpu_search'),
    path('search/rams/', RAMViewSet.as_view({'get': 'search'}), name='ram_search'),
    path('search/storages/', StorageViewSet.as_view({'get': 'search'}), name='storage_search'),
    path('search/builds/', BuildViewSet.as_view({'get': 'search'}), name='build_search'),
]
