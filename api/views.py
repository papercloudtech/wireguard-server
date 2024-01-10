from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .key_manager import generate_key
import requests
from api.models import Client


def login_view(request):
    if request.user.is_authenticated:
        return redirect('console')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('console')
        else:
            return render(request, 'api/login.html')
    return render(request, 'api/login.html')


@login_required(login_url='login')
def console_view(request):
    if request.method == "POST":
        pass
    current_configs = Client.objects.all()
    return render(request, 'api/dashboard.html')


def home(request):
    if request.user.is_authenticated:
        return redirect('console')
    return redirect('login')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


@login_required(login_url='login')
def manage_users(request):
    return render(request, 'api/users.html')


@login_required(login_url='login')
def performance_page(request):
    return render(request, 'api/performance.html')


@login_required(login_url='settings')
def manage_settings(request):
    return render(request, 'api/settings.html')
