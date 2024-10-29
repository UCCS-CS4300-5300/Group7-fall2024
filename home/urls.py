from django.urls import path,include
from . import views
from .models import *
from .views import login_or_register
from django.contrib.auth import views as auth_views

#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.

# add path functions here
urlpatterns = [
path('', views.index, name='index'),
path('builds/', views.build, name ='build'),
path('pre_build/', views.pre_built, name ='pre_build'),
path('login/', login_or_register, name='login_or_register'),
path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
path('register/', views.register_view, name='register'),



]