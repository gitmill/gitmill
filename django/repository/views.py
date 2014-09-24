from django.shortcuts import render
from user.decorators import user_view
from repository.decorators import repository_view

@user_view
@repository_view
def repository(request, user, repository, **kwargs):
    return render(request, 'app.html')
