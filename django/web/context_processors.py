from django.conf import settings

def all(request):
    return {
        'settings': settings,
        'request': request,
    }
