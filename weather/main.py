import requests
import json

from .geolocation import geolocator

def weather():
    geo=geolocator()
    local=geo.location()
    LAT=local.latitude
    LON=local.longitude
    res=json.loads(requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&lang=pt_br&units=metric&appid=5f0bbcdb65b09d1466b3e602f84fd109').content.decode('utf-8'))
    return {'temperature':int(res['main']['feels_like']), 'prev':res['weather'][0]['description']}
    
