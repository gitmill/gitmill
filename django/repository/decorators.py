from django.http import Http404
from repository.models import Repository
from functools import wraps

def repository_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            repository = Repository.objects.get(user=kwargs['user'], name=kwargs['name'])
        except Repository.DoesNotExist:
            raise Http404

        kwargs['repository'] = repository
        return func(request, *args, **kwargs)
    return wrapper
