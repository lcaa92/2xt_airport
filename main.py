#! /usr/bin/python3.6
import requests
from datetime import datetime, timedelta	

# # Sample Basic Auth Url with login values as username and password
url = "http://stub.2xt.com.br/air/airports/qhjvlDvYOwbbu9yq9Dq9DpzrprLAewmO"
username = "leandroca"
password = "tefvlD"
 
# Make a request to the endpoint using the correct auth values
auth_values = (username, password)
response = requests.get(url, auth=auth_values)
data = response.json()
 
# Convert JSON to dict and print
#print(response.json())

def iterate(dictionary):
    for key, value in dictionary.items():
    #    if isinstance(value, dict):
    #        iterate(value)
    #        continue
    	#print('key {!r} -> value {!r}'.format(key, value))
    	print(value['lat'])
 
#iterate(data)

count = 0
airports = []


for key, value in data.items():
	if count >= 20:
		break
	airports.append(value)
	count+=1

#print(airports)

for airport in airports:
	for airport in airports:
		print("ENTROU")
	print("----------------------------------------------")

date_search = datetime.today().date() - timedelta(days=40)
print(date_search)