from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from main.data import cities
from main.utils import get_uk_city_name, get_weather_by_city_name

def index(request:HttpRequest):
    return render(request, 'main/index.html', {'cities': cities})

def main(request:HttpRequest, city_name:str):
    data = get_weather_by_city_name(city_name)
    uk_city_name = get_uk_city_name(city_name)
    context= {
        'city-name': city_name,
        'uk_city_name': uk_city_name,
        'data': data,
        'weather_info': data["weather_info"]
    }
    return render(request, 'main/main.html', context)
