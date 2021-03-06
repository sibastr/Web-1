from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import register, profile


urlpatterns = [
    path('legacy/register/', register, name='register'),
    path('legacy/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('legacy/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('legacy/profile/', profile, name='profile'),
]

