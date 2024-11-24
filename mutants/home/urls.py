
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from django.urls import path, include
from . import views
from .models import *
from .views import *
from .views_api import *
from .views_render import *
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
path('add_to_build/<int:part_id>/<str:category>/', views.add_to_build, name='add_to_build'),
path('remove_from_build/<str:category>/', views.remove_from_build, name='remove_from_build'),
path('part_browser/', views.part_browser, name='part_browser'),

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
