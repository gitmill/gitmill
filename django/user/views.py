from django.http import HttpResponse
from user.decorators import user_view

@user_view
def user(request, user, **kwargs):
    return HttpResponse()
