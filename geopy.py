import xlsxwriter
import geopy
import pandas as pd
dirtyadr = pd.read_excel("finalstuff.xlsx")
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="sharan@gmail.com")
#from geopy.geocoders import GoogleV3
#geolocator = GoogleV3(api_key='AIzaSyAlgc_hOzENC3qY8r3JiIo7wYt9hHoXOWs')
def cleaner(address):
    location = geolocator.geocode(address)
    list = location.raw['display_name']
    print(location.raw['display_name'])
    lists = list.split(",")
    try:
        return location.raw['display_name']
    except:
        return ''

dirtyadr['Clean Address'] = dirtyadr.apply(lambda x: cleaner(x['raw address']),axis=1)

def get_orgname(address):
    location = geolocator.geocode(address)
    #print(location.raw)
    try:
        list = location.raw['display_name']
        lists = list.split(",")
        return lists[0]
    except:
        return ''
dirtyadr['organisation name'] = dirtyadr.apply(lambda x: get_orgname(x['raw address']),axis=1)

def locality(address):
    location = geolocator.geocode(address)
    #print(location.raw['display_name'])
    try:
        list = location.raw['display_name']
        lists = list.split(",")
        length=len(lists)
        return lists[length-5]
    except:
        return ''
dirtyadr['Locality/Area/Sector'] = dirtyadr.apply(lambda x: locality(x['raw address']),axis=1)
def get_dist_reg(address):
    location = geolocator.geocode(address)
    #print(location.raw['display_name'])
    try:
        list = location.raw['display_name']
        lists = list.split(",")
        length=len(lists)
        return lists[length-4]
    except:
        return ''
dirtyadr['District/Region'] = dirtyadr.apply(lambda x: get_dist_reg(x['raw address']),axis=1)
def get_pincode(address):
    location = geolocator.geocode(address)
    #print(location.raw['display_name'])
    try:
        list = location.raw['display_name']
        lists = list.split(",")
        length=len(lists)
        return lists[length-2]
    except:
        return ''
dirtyadr['Pincode'] = dirtyadr.apply(lambda x: get_pincode(x['raw address']),axis=1)
def get_state(address):
    location = geolocator.geocode(address)
    #print(location.raw['display_name'])
    try:
        list = location.raw['display_name']
        lists = list.split(",")
        length=len(lists)
        return lists[length-3]
    except:
        return ''
dirtyadr['State'] = dirtyadr.apply(lambda x: get_state(x['raw address']),axis=1)
def country(address):
    location = geolocator.geocode(address)
    #print(location.raw['display_name'])
    try:
        list = location.raw['display_name']
        lists = list.split(",")
        length=len(lists)
        return lists[length-1]
    except:
        return ''
dirtyadr['Country'] = dirtyadr.apply(lambda x: country(x['raw address']),axis=1)
dirtyadr
def latlong(address):
    location = geolocator.geocode(address)
    #print(location.raw['display_name'])
    try:
        return location.raw['lat'],location.raw['lon']
    except:
        return ''
dirtyadr['latitude&longtitude'] = dirtyadr.apply(lambda x: latlong(x['raw address']),axis=1)
dirtyadr





    


