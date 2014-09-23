from django.http import HttpResponse
from django.shortcuts import render

def app(request):
    return render(request, 'app.html')
