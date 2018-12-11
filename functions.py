from datetime import datetime, timedelta
from math import radians, cos, sin, asin, sqrt

def check_airport(airport_from, airport_to):
	#{'iata': 'BYO', 'city': 'Bonito', 'lat': -21.229445, 'lon': -56.456112, 'state': 'MS'}
	if ( airport_from['iata'] == airport_to['iata'] and 
		airport_from['city'] == airport_to['city'] and 
		airport_from['lat'] == airport_to['lat'] and 
		airport_from['lon'] == airport_to['lon'] and 
		airport_from['state'] == airport_to['state'] ):
		return False		
	return True

def calc_haversine(lon1, lat1, lon2, lat2):
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
    # return c * r
    return "{0:.2f}".format(round(c*r,2))

def convert_string_dateTime(dateTime1):
	return datetime.strptime(dateTime1.replace("T", " "), '%Y-%m-%d %H:%M:%S')

def tempo_voo(arrival_time, departure_time):
	time = convert_string_dateTime(arrival_time) - convert_string_dateTime(departure_time)
	time = time.seconds / 3600.0
	return time