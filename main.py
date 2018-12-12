#! /usr/bin/python3.6
import requests
from datetime import datetime, timedelta	
from utils.functions import check_airport, calc_haversine, convert_string_dateTime, tempo_voo
import psycopg2
from models.airport import AirportModel

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

for key, value in data.items():
	if count >= 20:
		break
	airports.append(value)
	count+=1
print("\n\n")	
print(airports)
print("\n\n")

for airport_from in airports:
	for airport_to in airports:
		if check_airport(airport_from, airport_to) == False:
			print("AEROPORTO NAO VERIFICADO: " + airport_to['iata'])
			continue
		
		#http://stub.2xt.com.br/air/search/:apikey:/:departure_airport:/:arrival_airport:/:departure_date:
		url_search = base_url_search+airport_from['iata']+'/'+airport_to['iata']+'/'+date_search
		response = requests.get(url_search, auth=auth_values)
		data_flight = response.json()

		#Distância linear em kms (Haversine)
			#Para cada avião:
				#Velocidade de voo aproximada.
				#Tarifa por km

		print("----------------------------------------------")
		print("Haversine")
		haversine = float(calc_haversine(data_flight['summary']['from']['lon'], data_flight['summary']['from']['lat'], data_flight['summary']['to']['lon'], data_flight['summary']['to']['lat']))
		
		print("Options Time")
		for option in data_flight['options']:
			print("##################")

			print( "DISTANCIA km" )
			print(haversine)

			print( "VELOCIDADE MEDIA" )
			time_flight = tempo_voo(option['arrival_time'], option['departure_time'])
			velocidade_media = haversine / time_flight
			print( "{0:.2f}".format(round( velocidade_media,2)) )

			print("Preço Tarifa por KM")
			km_tarifa = haversine / float(option['fare_price']) 
			print( "{0:.2f}".format(round( km_tarifa,2)) )

			print("##################")

		print("----------------------------------------------")
	print("#########################################")