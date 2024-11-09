from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# Define the non-API urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
    path('builds/', views.build, name='build'),
    path('pre_build/', views.pre_built, name='pre_build'),
    path('login/', views.login_or_register, name='login_or_register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('search/', views.search_pc_parts, name='search_pc_parts'),
    path('register/', views.register_view, name='register'),
]
