from django.urls import path,include
from . import views
from .models import *

#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.

# add path functions here
urlpatterns = [
path('', views.index, name='index'),


]