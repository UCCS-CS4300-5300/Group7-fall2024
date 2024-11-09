from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import BuildViewSet, MotherboardViewSet, CPUViewSet, RAMViewSet, StorageViewSet, get_mobos, get_cpus, get_builds, get_rams, get_storages, get_builds_user, search_motherboards, search_cpus, search_rams, search_storages

# Define the router and register the viewsets
router = DefaultRouter()
router.register(r'builds', BuildViewSet)
router.register(r'motherboards', MotherboardViewSet)
router.register(r'cpus', CPUViewSet)
router.register(r'rams', RAMViewSet)
router.register(r'storages', StorageViewSet)

# Define the API urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # API routes with router
    path('motherboards/', get_mobos, name='motherboards'),
    path('cpus/', get_cpus, name='cpus'),
    path('builds/', get_builds, name='builds'),
    path('rams/', get_rams, name='rams'),
    path('storages/', get_storages, name='storages'),
    path('user_builds/<int:user_id>/', get_builds_user, name='user_builds'),
    path('search/motherboards/', search_motherboards, name='search_motherboards'),
    path('search/cpus/', search_cpus, name='search_cpus'),
    path('search/rams/', search_rams, name='search_rams'),
    path('search/storages/', search_storages, name='search_storages'),
]
