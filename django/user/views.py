from django.shortcuts import render
from user.decorators import user_view

@user_view
def user(request, user, **kwargs):
    return render(request, 'app.html')
