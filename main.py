#! /usr/bin/python3.6
import requests
from datetime import datetime, timedelta	
from math import radians, cos, sin, asin, sqrt

# # Sample Basic Auth Url with login values as username and password
url_airports = "http://stub.2xt.com.br/air/airports/qhjvlDvYOwbbu9yq9Dq9DpzrprLAewmO"
username = "leandroca"
password = "tefvlD"
api_key = "qhjvlDvYOwbbu9yq9Dq9DpzrprLAewmO"
base_url_search = "http://stub.2xt.com.br/air/search/"+api_key+"/"
 
# Make a request to the endpoint using the correct auth values
auth_values = (username, password)
response = requests.get(url_airports, auth=auth_values)
data = response.json()

def check_airport(airport_from, airport_to):
	#{'iata': 'BYO', 'city': 'Bonito', 'lat': -21.229445, 'lon': -56.456112, 'state': 'MS'}
	if ( airport_from['iata'] == airport_to['iata'] and 
		airport_from['city'] == airport_to['city'] and 
		airport_from['lat'] == airport_to['lat'] and 
		airport_from['lon'] == airport_to['lon'] and 
		airport_from['state'] == airport_to['state'] ):
		return False		
	return True

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

count = 0
airports = []

date_search = (datetime.today().date() - timedelta(days=40)).strftime('%Y-%m-%d')

for key, value in data.items():
	if count >= 20:
		break
	airports.append(value)
	count+=1

for airport_from in airports:
	for airport_to in airports:
		if check_airport(airport_from, airport_to) == False:
			print("AEROPORTO NAO VERIFICADO: " + airport_to['iata'])
			continue
		#http://stub.2xt.com.br/air/search/:apikey:/:departure_airport:/:arrival_airport:/:departure_date:
		url_search = base_url_search+airport_from['iata']+'/'+airport_to['iata']+'/'+date_search
		response = requests.get(url_search, auth=auth_values)
		data_flight = response.json()
		print("----------------------------------------------")
		print("Haversine "+haversine(data_flight['summary']['from']['lon'], data_flight['summary']['from']['lat'], data_flight['summary']['to']['lon'], data_flight['summary']['to']['lat']))
		print("----------------------------------------------")
	print("#########################################")