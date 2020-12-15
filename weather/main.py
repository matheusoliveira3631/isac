import requests
import json

from .geolocation import geolocator

geo=geolocator()
local=geo.location()
LAT=local.latitude
LON=local.longitude
#=========================================><======================================#

class Weather:

    def __init__(self):
        global res
        res=json.loads(requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&lang=pt_br&units=metric&appid=5f0bbcdb65b09d1466b3e602f84fd109').content.decode('utf-8'))

    def weather(self):
        weather={'temperature':int(res['main']['feels_like']), 'prev':res['weather'][0]['description']}
        return weather

