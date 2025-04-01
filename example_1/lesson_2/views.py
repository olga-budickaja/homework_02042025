from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request, 'index.html')


def bio(request, username):
    print(username)
    return render(request, 'index.html')


def special_case_2003(request):
    print(request)
    return HttpResponse('special_case_2003')


def year_archive(request, year):
    print(request)
    print(year)
    print(type(year))
    if year == 2003:
        return HttpResponse('special_case_2003')
    return HttpResponse(f'{year}')

def home(request: HttpRequest):
    return HttpResponse("This is the home page")

def book(request: HttpRequest, title):
    return HttpResponse(f"This is the book page with the title: {title}")
