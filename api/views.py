from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .key_manager import generate_key
import requests


def login_view(request):
    if request.user.is_authenticated:
        redirect('/dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("Logged in")
            return render(request, 'api/dashboard.html')
        else:
            return render(request, 'api/login.html')
    return render(request, 'api/login.html')


@login_required(login_url='login')
def console_view(request):
    return render(request, 'api/dashboard.html')


def get_config(request):
    config_file = generate_key("10.0.0.0", requests.get('https://checkip.amazonaws.com').text.strip())
    return HttpResponse(config_file, content_type="text/plain")
