from django.urls import path, include
from . import views
from .models import *
from .views import *
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.

router = DefaultRouter()
router.register(r'builds', BuildViewSet)

# add path functions here
urlpatterns = [

path('', views.index, name='index'),
path('builds/', views.build, name ='build'),
path('pre_build/', views.pre_built, name ='pre_build'),
path('login/', login_or_register, name='login_or_register'),
path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
path('search/', views.search_pc_parts, name='search_pc_parts'),
path('register/', views.register_view, name='register'),

# Include the router URLs for the API
path('api/', include(router.urls)),  # Prefix API routes with /api/
path('api/get_builds/', get_builds, name='get_builds'),
path('api/get_mobos/', get_mobos, name='get_mobos'),

]