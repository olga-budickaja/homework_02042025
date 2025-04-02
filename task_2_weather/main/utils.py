import requests
from config.settings import WEATHER_API_KEY, WEATHER_API_URL
from main.data import cities


def get_weather_by_city_name(city_name: str):
    url = f'{WEATHER_API_URL}{city_name}&appid={WEATHER_API_KEY}&units=metric&lang=uk'
    response = requests.get(url)
    res = response.json()

    data = {
        "city": city_name,
        "description": res["weather"][0]["description"],
        "weather_info": [
            {"name": "Температура", "value": round(res["main"]["temp"]), "unit": "°C"},
            {"name": "Тиск", "value": res["main"]["pressure"], "unit": "hPa"},
            {"name": "Вологість", "value": res["main"]["humidity"], "unit": "%"},
            {"name": "Швидкість вітру", "value": res["wind"]["speed"], "unit": "м/с"},
        ],
        "list_emoji": ["🌡", "🌬", "💧", "💨"],
    }
    return data

def get_uk_city_name(city_name:str):
    return cities.get(city_name, {}).get("uk", "Місто не знайдено")
