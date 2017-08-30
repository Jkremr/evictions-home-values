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
    def __init__(self, regionid, name, zurl, meanvalue, currency, lat, lng, prices):
        self.regionid = regionid 
        self.name = name
        self.zurl = zurl
        self.meanvalue = meanvalue
        self.currency = currency
        self.lat = lat
        self.lng = lng
        self.prices = prices

city = 'San Francisco'
state = 'CA'
baseUrl = 'http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id='
url = baseUrl + zillowApiKey + '&state=' + state + '&city=' + city.replace(" ", "+") + '&childtype=neighborhood'
r = req.get(url)

colNames = ('regionid', 'name', 'url', 'meanvalue', 'currency', 'latitude', 'longitude')
neighborhoods = pd.DataFrame(columns = colNames)

# Call Zillow API to get neighborhood data for our city. 

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

dls = 'https://www.zillow.com/market-report/time-series/274552/mission-san-francisco-ca.xls?m=zhvi_plus_forecast'
resp = req.get(dls)
with open('mission-san-francisco-ca.xls', 'wb') as output:
    output.write(resp.content)

property_values = pd.read_excel('mission-san-francisco-ca.xls', sheetname='All Homes', skiprows = 1)

neighborhoods = neighborhoods.merge(property_values, how='left', left_on='name', right_on='Region Name')

neighborhoods.to_csv('neighborhoods.csv')
# Create kdtree
_neighborhoods_kdtree = kdtree.create(dimensions=2)
CITY_NEIGHBORHOODS_dict = {}

# Add neighborhood centroids into kdtree
for index, row in neighborhoods.iterrows():
    lat = float(row[5])
    lng = float(row[6])
    city_coordinate_key = (lat, lng)
    _neighborhoods_kdtree.add(city_coordinate_key)
    propvalues = {
    'Aug2007':row[10],
    'Sep2007':row[11],
    'Oct2007':row[12],
    'Nov2007':row[13],
    'Dec2007':row[14],
    'Jan2008':row[15],
    'Feb2008':row[16],
    'Mar2008':row[17],
    'Apr2008':row[18],
    'May2008':row[19],
    'Jun2008':row[20],
    'Jul2008':row[21],
    'Aug2008':row[22],
    'Sep2008':row[23],
    'Oct2008':row[24],
    'Nov2008':row[25],
    'Dec2008':row[26],
    'Jan2009':row[27],
    'Feb2009':row[28],
    'Mar2009':row[29],
    'Apr2009':row[30],
    'May2009':row[31],
    'Jun2009':row[32],
    'Jul2009':row[33],
    'Aug2009':row[34],
    'Sep2009':row[35],
    'Oct2009':row[36],
    'Nov2009':row[37],
    'Dec2009':row[38],
    'Jan2010':row[39],
    'Feb2010':row[40],
    'Mar2010':row[41],
    'Apr2010':row[42],
    'May2010':row[43],
    'Jun2010':row[44],
    'Jul2010':row[45],
    'Aug2010':row[46],
    'Sep2010':row[47],
    'Oct2010':row[48],
    'Nov2010':row[49],
    'Dec2010':row[50],
    'Jan2011':row[51],
    'Feb2011':row[52],
    'Mar2011':row[53],
    'Apr2011':row[54],
    'May2011':row[55],
    'Jun2011':row[56],
    'Jul2011':row[57],
    'Aug2011':row[58],
    'Sep2011':row[59],
    'Oct2011':row[60],
    'Nov2011':row[61],
    'Dec2011':row[62],
    'Jan2012':row[63],
    'Feb2012':row[64],
    'Mar2012':row[65],
    'Apr2012':row[66],
    'May2012':row[67],
    'Jun2012':row[68],
    'Jul2012':row[69],
    'Aug2012':row[70],
    'Sep2012':row[71],
    'Oct2012':row[72],
    'Nov2012':row[73],
    'Dec2012':row[74],
    'Jan2013':row[75],
    'Feb2013':row[76],
    'Mar2013':row[77],
    'Apr2013':row[78],
    'May2013':row[79],
    'Jun2013':row[80],
    'Jul2013':row[81],
    'Aug2013':row[82],
    'Sep2013':row[83],
    'Oct2013':row[84],
    'Nov2013':row[85],
    'Dec2013':row[86],
    'Jan2014':row[87],
    'Feb2014':row[88],
    'Mar2014':row[89],
    'Apr2014':row[90],
    'May2014':row[91],
    'Jun2014':row[92],
    'Jul2014':row[93],
    'Aug2014':row[94],
    'Sep2014':row[95],
    'Oct2014':row[96],
    'Nov2014':row[97],
    'Dec2014':row[98],
    'Jan2015':row[99],
    'Feb2015':row[100],
    'Mar2015':row[101],
    'Apr2015':row[102],
    'May2015':row[103],
    'Jun2015':row[104],
    'Jul2015':row[105],
    'Aug2015':row[106],
    'Sep2015':row[107],
    'Oct2015':row[108],
    'Nov2015':row[109],
    'Dec2015':row[110],
    'Jan2016':row[111],
    'Feb2016':row[112],
    'Mar2016':row[113],
    'Apr2016':row[114],
    'May2016':row[115],
    'Jun2016':row[116],
    'Jul2016':row[117],
    'Aug2016':row[118],
    'Sep2016':row[119],
    'Oct2016':row[120],
    'Nov2016':row[121],
    'Dec2016':row[122],
    'Jan2017':row[123],
    'Feb2017':row[124],
    'Mar2017':row[125],
    'Apr2017':row[126],
    'May2017':row[127],
    'Jun2017':row[128],
    'Jul2017':row[129]
    }
    n = Neighborhood(row[0], row[1], row[2], row[3], row[4], row[5], row[6], propvalues)
    CITY_NEIGHBORHOODS_dict[city_coordinate_key] = n


def nearest_neighborhood(latitude, longitude):
    nearest_neighborhood_coordinate = _neighborhoods_kdtree.search_nn((latitude, longitude, ))
    return CITY_NEIGHBORHOODS_dict[nearest_neighborhood_coordinate[0].data]

