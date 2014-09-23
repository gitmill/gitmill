from django.contrib.auth import authenticate
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from user.models import Key
from functools import wraps
import base64
import logging

def user_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            user = User.objects.get(username=kwargs['username'])
        except User.DoesNotExist:
            raise Http404

        kwargs['user'] = user
        return func(request, *args, **kwargs)
    return wrapper

def key_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            key = Key.objects.get(id=kwargs['id'])
        except Key.DoesNotExist:
            raise Http404

        kwargs['key'] = key
        return func(request, *args, **kwargs)
    return wrapper

def authenticated_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        request.user = None

        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        if authorization and authorization.startswith('Basic '):
            parts = base64.b64decode(authorization.split(None, 1)[1]).split(':', 1)
            if len(parts) == 2:
                username, password = parts
                user = authenticate(username=username, password=password)
                if user and user.is_active:
                   request.user = user
                   logging.warn('user: authenticated: id = %d, username = %s' % (user.id, user.username))

        response = func(request, *args, **kwargs)

        if response.status_code == 403 and not request.user:
            response = HttpResponse(status=401)
            response['WWW-Authenticate'] = 'Basic realm=""'

        return response
    return wrapper
