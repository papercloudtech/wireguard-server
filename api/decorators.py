from functools import wraps
from django.http import JsonResponse
from .models import ApiKey

def api_key_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            return JsonResponse({'error': 'API key missing'}, status=401)

        try:
            key = ApiKey.objects.get(key=api_key)
            if key.is_expired():
                return JsonResponse({'error': 'API key expired'}, status=401)
        except ApiKey.DoesNotExist:
            return JsonResponse({'error': 'Invalid API key'}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view

