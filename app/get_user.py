import requests
import json

def get_flight():
    url = requests.get('https://api.infiniteflight.com/public/v2/flights/7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw')
    responser = json.loads(url.text)
    return responser


def get_ifatc():
    url = requests.get('https://api.infiniteflight.com/public/v2/atc/7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856?apikey=nvo8c790hfa9q3duho2jhgd2jf8tgwqw')
    responser = json.loads(url.text)
    return responser
    
def get_icao():
    url = requests.get('https://raw.githubusercontent.com/Dalmocabral/infinteflightaerobrasil_atc/master/exceljson.json')
    responser = json.loads(url.text)
    return responser


