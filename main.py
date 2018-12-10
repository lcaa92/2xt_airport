#! /usr/bin/python3.6
import requests

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
        if isinstance(value, dict):
            iterate(value)
            continue
    print('key {!r} -> value {!r}'.format(key, value))
 
#iterate(data)


for item in data:
	print ("Item: " + item)

	    