from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from io import StringIO
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
    current_configs = Client.objects.all()
    return render(request, 'api/users.html', {'clients': current_configs})


@login_required(login_url='login')
def performance_page(request):
    return render(request, 'api/performance.html')


@login_required(login_url='login')
def manage_settings(request):
    return render(request, 'api/settings.html')


@login_required(login_url='login')
def download_config(request, pk):
    current_config = Client.objects.get(pk=pk)
    response = HttpResponse(current_config.config, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{current_config.name}.conf"'
    return response
