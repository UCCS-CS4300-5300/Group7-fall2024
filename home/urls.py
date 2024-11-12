from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('pre_built/', views.pre_built, name='pre_built'),
    path('build/', views.build, name='build'),
    path('part_browser/', views.part_browser, name='part_browser'),
    path('account_page/', views.account_page, name='account_page'),
    path('', views.index, name='index'),
    path('search_pc_parts/', views.search_pc_parts, name='search_pc_parts'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),  # Ensure this line is correct
]
