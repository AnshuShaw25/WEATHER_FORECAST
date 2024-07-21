"""from django.shortcuts import render
import requests

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "f68e1cbabe7631675a9fdc8e23d0b6d4"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_city_image(city):
    unsplash_url = "https://api.unsplash.com/search/photos"
    unsplash_api_key = "vdP4Wt6JUspSVQilU5exiem7vR2mxBrQrK-tcuZdc0k"
    parameters = {
        'query': city,
        'client_id': unsplash_api_key,
        'per_page': 1
    }
    response = requests.get(unsplash_url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['full']
    return None

def home(request):
    weather = None
    country = None
    weather_description = None
    wind_speed = None
    pressure = None
    humidity = None
    temperature = None
    city = request.GET.get('city')
    icon_url = 'https://openweathermap.org/img/wn/10d@2x.png'
    background_image_url = '/static/images/bg_image.jpg'  # Default background image

    if city:
        weather_data_result = get_weather(city)
        if weather_data_result is not None:
            icon_id = weather_data_result['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            # Extracting Details
            weather = weather_data_result['weather'][0]['main']
            weather_description = weather_data_result['weather'][0]['description']
            city = weather_data_result['name']
            country = weather_data_result['sys']['country']
            wind_speed = weather_data_result['wind']['speed']
            pressure = weather_data_result['main']['pressure']
            humidity = weather_data_result['main']['humidity']
            temperature = weather_data_result['main']['temp']
            # Fetch city image
            city_image_url = get_city_image(city)
            if city_image_url:
                background_image_url = city_image_url
        else:
            return render(request, 'index.html')

    return render(request, 'index.html', {
        'icon_url': icon_url,
        'weather': weather,
        'weather_description': weather_description,
        'city': city,
        'country': country,
        'wind_speed': wind_speed,
        'pressure': pressure,
        'humidity': humidity,
        'temperature': temperature,
        'background_image_url': background_image_url,
    })
    """
from django.shortcuts import render
import requests

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "f68e1cbabe7631675a9fdc8e23d0b6d4"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_city_image(city):
    pexels_url = "https://api.pexels.com/v1/search"
    pexels_api_key = "enOPmJQDBWUceSzpmh3mpYz6qNA7iCCY11FFOdzWWv2vPJihKcAqFIy7"
    headers = {
        'Authorization': pexels_api_key
    }
    parameters = {
        'query': city,
        'per_page': 1
    }
    response = requests.get(pexels_url, headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            return data['photos'][0]['src']['original']
    return None

def home(request):
    weather = None
    country = None
    weather_description = None
    wind_speed = None
    pressure = None
    humidity = None
    temperature = None
    city = request.GET.get('city')
    icon_url = 'https://openweathermap.org/img/wn/10d@2x.png'
    background_image_url = '/static/images/bg_image.jpg'  # Default background image

    if city:
        weather_data_result = get_weather(city)
        if weather_data_result is not None:
            icon_id = weather_data_result['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            # Extracting Details
            weather = weather_data_result['weather'][0]['main']
            weather_description = weather_data_result['weather'][0]['description']
            city = weather_data_result['name']
            country = weather_data_result['sys']['country']
            wind_speed = weather_data_result['wind']['speed']
            pressure = weather_data_result['main']['pressure']
            humidity = weather_data_result['main']['humidity']
            temperature = weather_data_result['main']['temp']
            
            if city.lower() == 'patna':
                # Use the predefined image for Patna
                background_image_url = '/static/images/patna.jpg'
            else:
                # Fetch city image for other cities
                city_image_url = get_city_image(city)
                if city_image_url:
                    background_image_url = city_image_url
        else:
            return render(request, 'index.html')

    return render(request, 'index.html', {
        'icon_url': icon_url,
        'weather': weather,
        'weather_description': weather_description,
        'city': city,
        'country': country,
        'wind_speed': wind_speed,
        'pressure': pressure,
        'humidity': humidity,
        'temperature': temperature,
        'background_image_url': background_image_url,
    })
