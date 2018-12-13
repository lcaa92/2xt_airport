#! /usr/bin/python3.6
import requests
from datetime import datetime, timedelta	
from utils.functions import check_airport, calc_haversine, convert_string_dateTime, tempo_voo
import psycopg2
from models.airport import AirportModel
from models.routes import RouteModel

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

count = 0
airports = []

date_search = (datetime.today().date() - timedelta(days=40)).strftime('%Y-%m-%d')

#Montando array com aeroportos
print("###### Cadastrando aeroportos")
for key, value in data.items():
	if count >= 20:
		break
	airports.append(value)
	AirportModel.create(value)
	count+=1
print("###### Aeroportos cadastrados")

print("###### Cadastrando rotas entre aeroportos")
for airport_from in airports:
	for airport_to in airports:
		if check_airport(airport_from, airport_to) == False:
			continue

		#http://stub.2xt.com.br/air/search/:apikey:/:departure_airport:/:arrival_airport:/:departure_date:
		url_search = base_url_search+airport_from['iata']+'/'+airport_to['iata']+'/'+date_search
		response = requests.get(url_search, auth=auth_values)
		data_flight = response.json()

		if len(data_flight['options']) < 1:
			continue

		haversine = float(calc_haversine(data_flight['summary']['from']['lon'], data_flight['summary']['from']['lat'], data_flight['summary']['to']['lon'], data_flight['summary']['to']['lat']))
		
		lowest_price = None
		time_flight = None
		km_tarifa = None
		aircraft = None

		for option in data_flight['options']:

			if lowest_price is None:
				lowest_price = option['fare_price']
				time_flight = tempo_voo(option['arrival_time'], option['departure_time'])
				km_tarifa = haversine / float(option['fare_price']) 
				aircraft = option['aircraft']['model']
				continue

			if option['fare_price'] < lowest_price:
				lowest_price = option['fare_price']
				time_flight = tempo_voo(option['arrival_time'], option['departure_time'])
				km_tarifa = haversine / float(option['fare_price']) 
				aircraft = option['aircraft']['model']

		route = {}
		route['url_mockup'] = url_search
		route['distance'] = str(haversine)
		route['lowest_price'] = str(lowest_price)
		route['km_price'] = "{0:.2f}".format(round( km_tarifa,2))
		route['aircraft'] = aircraft
		route['time_flight'] = "{0:.2f}".format(round( time_flight,2))
		route['average_speed'] = "{0:.2f}".format(round( haversine / time_flight,2))

		RouteModel.create(route)

print("###### Rotas cadastradas")