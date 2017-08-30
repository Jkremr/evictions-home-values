import requests as req
import pandas as pd
import numpy as np
import kdtree
import xml.etree.ElementTree as ET
from apikeys import zillowApiKey

class Neighborhood:
    '''
    Neighborhood contains information about a Zillow neighborhood.
    '''
    def __init__(self, regionid, name, zurl, meanvalue, currency, lat, lng):
        self.regionid = regionid 
        self.name = name
        self.zurl = zurl
        self.meanvalue = meanvalue
        self.currency = currency
        self.lat = lat
        self.lng = lng

city = 'San Francisco'
state = 'CA'
baseUrl = 'http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id='
url = baseUrl + zillowApiKey + '&state=' + state + '&city=' + city.replace(" ", "+") + '&childtype=neighborhood'
r = req.get(url)

colNames = ('regionid', 'name', 'url', 'meanvalue', 'currency', 'latitude', 'longitude')
neighborhoods = pd.DataFrame(columns = colNames)

# Call API to get neighborhood data for our city. 

tree = ET.fromstring(r.content)
for region in tree[2][2].findall('region'):
    regionid = region.find('id').text
    name = region.find('name').text 
    try: 
        region.find('zindex').attrib
        currency = region.find('zindex').attrib['currency']
        meanvalue = region.find('zindex').text
    except AttributeError:
        currency = 'USD'
        meanvalue = 0
    zurl = region.find('url').text 
    latitude = str(region.find('latitude').text)
    longitude = region.find('longitude').text 
    neighborhoods.loc[len(neighborhoods)+1] = [regionid, name, zurl, meanvalue, currency, latitude, longitude]



# _current_dir, _current_filename = os.path.split(__file__)
# _world_cities_csv_path = os.path.join(_current_dir, 'worldcities.csv')
_neighborhoods_kdtree = kdtree.create(dimensions=2)
CITY_NEIGHBORHOODS_dict = {}

# with open(_world_cities_csv_path, 'r') as csv_file:
#     cities = csv.reader(csv_file)

#     # discard the headers
#     cities.__next__()

    # populate geo points into kdtree
for index, row in neighborhoods.iterrows():
    lat = float(row[5])
    lng = float(row[6])
    city_coordinate_key = (lat, lng)
    _neighborhoods_kdtree.add(city_coordinate_key)
    n = Neighborhood(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    CITY_NEIGHBORHOODS_dict[city_coordinate_key] = n


def nearest_neighborhood(latitude, longitude):
    nearest_neighborhood_coordinate = _neighborhoods_kdtree.search_nn((latitude, longitude, ))
    return CITY_NEIGHBORHOODS_dict[nearest_neighborhood_coordinate[0].data]

