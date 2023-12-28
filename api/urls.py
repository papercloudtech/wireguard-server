from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('console', views.console_view, name='console'),
]
