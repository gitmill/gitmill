from django.conf.urls import patterns, url
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from user.decorators import user_view

def users(request):
    return JsonResponse({
        'users': [],
    })

@user_view
def user(request, user, **kwargs):
    repositories = user.repositories.all()

    return JsonResponse({
        'user': {
            'id': user.username,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'repositories': [user.username + '/' + repository.name for repository in repositories],
        },
        'repositories': [
            {
                'id': user.username + '/' + repository.name,
                'username': user.username,
                'name': repository.name,
                'description': repository.description,
                'user': user.username,
            }
            for repository in repositories
        ]
    })

urlpatterns = patterns('',
    url(r'^users$', users),
    url(r'^users/(?P<username>[A-Za-z0-9_@+.\-]{1,30})$', user),
)

