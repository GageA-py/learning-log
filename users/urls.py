"""Define urls patterns for users"""

from django.urls import path, include
from django.contrib import auth
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
     path('logout/', auth_views.LogoutView.as_view(next_page='learning_logs:index'), name='logout'),
     # Registration page
     path('register/', views.register, name='register'),
]