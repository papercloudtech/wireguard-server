from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from api.models import Client
from django.http import JsonResponse
from .decorators import api_key_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
    if request.method == "POST":
        newuser = Client.objects.create(name=request.POST['username'])
        newuser.save()
        return redirect('users')

    current_configs = Client.objects.all().order_by("id")
    paginated_configs = Paginator(current_configs, request.GET.get("per_page", 10)).get_page(
        request.GET.get("page", 1)
    )

    return render(request, 'api/users.html', {'clients': paginated_configs})


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


@login_required(login_url='login')
def delete_config(request, pk):
    current_config = Client.objects.get(pk=pk)
    current_config.delete()
    current_configs = Client.objects.all()
    return redirect('users')

@csrf_exempt
@api_key_required
def manage_users_api(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if not name:
            return JsonResponse({'error': 'Missing user name'}, status=400)

        new_user = Client.objects.create(name=name)
        new_user.save()

        return JsonResponse({'message': 'User created', 'name': new_user.name, 'ip': new_user.ip_address}, status=201)

    elif request.method == "GET":
        clients = Client.objects.all().values('id', 'name', 'ip_address')
        return JsonResponse(list(clients), safe=False, status=200)
    
    return JsonResponse({'error': 'Invalid method'}, status=405)
