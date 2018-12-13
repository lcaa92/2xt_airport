from .connectorDatabase import ConnectorDatabase

class RouteModel:

	def create(route):
		sql = "INSERT INTO routes (url_mockup, distance, lowest_price, km_price, aircraft, time_flight, average_speed) VALUES ('"+route['url_mockup']+"', '"+route['distance']+"', '"+route['lowest_price']+"', '"+route['km_price']+"', '"+route['aircraft']+"', '"+route['time_flight']+"', '"+route['average_speed']+"');"
		ConnectorDatabase.runSql(sql)
