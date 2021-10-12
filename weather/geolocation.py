import socket
import requests
import json

from ip2geotools.databases.noncommercial import DbIpCity, HostIP, MaxMindGeoLite2City


class geolocator:
    def __init__(self):
        pass
    
    def get_ip(self):
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify = True)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        data = response.json()

        return data['ip']

    def location(self):
        local=self.get_ip()
        try:
            data = DbIpCity.get(local, api_key='free')
        except:
            try:
                data = HostIP.get(local, api_key='free')
            except:
                try:
                    data = MaxMindGeoLite2City.get(local, api_key='free')
                except:
                    return False
        return data
