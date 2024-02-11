from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('console', views.console_view, name='console'),
    path('console/users', views.manage_users, name='users'),
    path('console/performance', views.performance_page, name='performance'),
    path('console/settings', views.manage_settings, name='settings'),
    path('', views.home, name='home'),
    path('config/<int:pk>', views.download_config, name='create_config'),
    path('config/delete/<int:pk>', views.delete_config, name='delete_config'),
    path('logout', views.logout_user, name='logout'),
]
