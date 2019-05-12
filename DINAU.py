from geopy.geocoders import Nominatim
from datetime import  datetime, timedelta
import os
import requests, sys

if len(sys.argv) == 2:
    print()
else:
    print('Not enough Commant Line Arguments! \n Proper use \"python DINAU.py \"address here\" \" ')
    sys.exit()

# get api key
while True:
    try:
        if os.stat("API_key.txt").st_size < 32:
            f = open('API_key.txt','w+')
            while True:
                keyInput = input('Please input your Dark Sky API Key: ')
                if len(keyInput) == 32:
                    f.write(keyInput)
                    break
                else:
                    print('Key Invalid!')
        else:
            key = open('API_key.txt','r').readline().rstrip('\n')
            break
    except FileNotFoundError:
        print('API_key.txt not found. Creating file.')
        f = open('API_key.txt','w+')

geolocator = Nominatim(user_agent="DoINeddAnUmbreella")
location =  geolocator.geocode(sys.argv[1], language='en_US')
latitude = str(location.latitude)
longitude = str(location.longitude)
exclusions = 'exclude=currently,minutely,hourly,alerts&amp;units='#the default units is US Metric but i might as well specify

request = requests.get("https://api.darksky.net/forecast/"+key+"/"+latitude+","+longitude)
JSON_REQ = request.json()

rainChance = JSON_REQ['daily']['data'][0]['precipProbability']
rainChance *= 100

print(rainChance)
