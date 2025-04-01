from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def bio(request: HttpRequest, username=""):
    return HttpResponse(f"This is the bio page with the user bio: {username}")
