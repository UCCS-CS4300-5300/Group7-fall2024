from django.urls import path, include
from . import views
from .models import *
from .views import *
from .views_api_call import *
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

# paths for api endpoints
path('api/', include(router.urls)),  # Prefix API routes with /api/
path('api/get_builds/', get_builds, name='get_builds'),
path('api/get_builds/user<int:user_id>/', get_builds_user, name='get_builds'), # get builds belonging to logged in user
path('api/get_mobos/', get_mobos, name='get_mobos'),
path('api/get_cpus/', get_cpus, name='get_cpus'),
path('api/get_rams/', get_rams, name='get_rams'),
path('api/get_storages/', get_storages, name='get_storages'),

# see views_api_call.py to see the views that are related to these urls.
# the views referenced by these urls will call the api endpoints
path('builds_list/', call_builds_view, name='call_builds_view'),
path('builds_list/user/', call_user_builds_view, name='call_user_builds_view'),
path('motherboards/', call_motherboards_view, name='call_motherboards_view'),
path('cpus/', call_cpus_view, name='call_cpus_view'),
path('rams/', call_rams_view, name='call_rams_view'),
path('storages/', call_storages_view, name='call_storages_view'),

# create an add cpu, ram, storage, mobo, etc ... paths that looks like this:
# path('build/<int:build_id>/add_cpu/', , ),
# path('build/<int:build_id>/add_mobo/', , ),
# path('build/<int:build_id>/add_ram/', , ),
# path('build/<int:build_id>/add_storage/', , ),


]