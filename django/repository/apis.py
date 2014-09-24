from django.conf.urls import patterns, url
from django.http import Http404, JsonResponse
from user.decorators import user_view
from repository.decorators import repository_view

def repositories(request):
    return JsonResponse({
        'users': [],
    })

@user_view
@repository_view
def repository(request, user, repository, **kwargs):
    return JsonResponse({
        'repository': {
            'id': user.username + '/' + repository.name,
            'username': user.username,
            'name': repository.name,
            'description': repository.description,
            'user': user.username,
        },
        'users': [{
            'id': user.username,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'repositories': [user.username + '/' + repository.name for repository in user.repositories.all()],
        }],
    })

urlpatterns = patterns('',
    url(r'^repositories$', repositories),
    url(r'^repositories/(?P<username>[A-Za-z0-9_@+.\-]{1,30})/(?P<name>[^\x00-\x2c\x2f\x3a-\x40\x5b-\x5e\x60\x7b-\x7f\s]{1,64})$', repository),
)

