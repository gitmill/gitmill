from django.http import HttpResponse
from user.decorators import user_view
from repository.decorators import repository_view

@user_view
@repository_view
def repository(request, user, repository, **kwargs):
    return HttpResponse()
