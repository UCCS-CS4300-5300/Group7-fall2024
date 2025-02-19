from . import views
from .views import login_or_register
from .views_render import (
    call_motherboards_view, call_cpus_view, call_builds_view,
    call_user_builds_view, call_rams_view, call_storages_view
)
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path  # Importing path function
from .views_api import BuildViewSet  # Importing BuildViewSet

# path function defines a url pattern
# '' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.

router = DefaultRouter()
router.register(r'builds', BuildViewSet)

# add path functions here
urlpatterns = [

    path('', views.index, name='index'),
    path('builds/', views.build, name='build'),
    path('login/', login_or_register, name='login_or_register'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search_pc_parts, name='search_pc_parts'),
    path('register/', views.register_view, name='register'),
    path('add_to_build/<int:part_id>/<str:category>/', views.add_to_build, name='add_to_build'),
    path('remove_from_build/<str:category>/', views.remove_from_build, name='remove_from_build'),
    path('part_browser/', views.part_browser, name='part_browser'),
    path('account_page/', views.account_page, name='account_page'),
    path('save_build/', views.save_build, name='save_build'),
    path('delete_build/<int:build_id>/', views.delete_build, name='delete_build'),
    path('edit_build/<int:build_id>/', views.edit_build, name='edit_build'),
    path('view_build/<int:build_id>/', views.view_build, name='view_build'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:item_id>/<str:category>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/add_build/', views.add_build_to_cart, name='add_build_to_cart'),
    path('cart/add_saved_build/<int:build_id>/', views.add_saved_build_to_cart, name='add_saved_build_to_cart'),
    path("payment/create/", views.create_paypal_payment, name="create_paypal_payment"),
    path('paypal/checkout/', views.create_paypal_payment, name='checkout_with_paypal'),
    path("payment/execute/", views.execute_paypal_payment, name="execute_paypal_payment"),
    path('test-paypal/', views.test_paypal, name='test_paypal'),
    path('purchase-confirmed/', views.purchase_confirmed, name='purchase_confirmed'),
    path('build_error/<int:build_id>/', views.build_error, name='build_error'),



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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
