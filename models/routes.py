from .connectorDatabase import ConnectorDatabase

class RouteModel:

	def create(route):
		sql = "INSERT INTO routes (url_mockup, distance, lowest_price, km_price, aircraft, time_flight, average_speed, airport_from, airport_to) VALUES ('"+route['url_mockup']+"', '"+route['distance']+"', '"+route['lowest_price']+"', '"+route['km_price']+"', '"+route['aircraft']+"', '"+route['time_flight']+"', '"+route['average_speed']+"', '"+route['airport_from']+"', '"+route['airport_to']+"');"
		ConnectorDatabase.runSql(sql)

	def getViagensLongasKm():
		sql = "SELECT * FROM routes ORDER BY distance DESC LIMIT 30;"
		result_db = ConnectorDatabase.runSqlConsulta(sql)
		result = []
		for rs in result_db:
			obj = {
				'id': rs[0],
				'url_mockup': rs[1],
				'distance': str(rs[2]),
				'lowest_price': str(rs[3]),
				'km_price': str(rs[4]),
				'aircraft': rs[5],
				'time_flight': str(rs[6]),
				'average_speed': str(rs[7]),
				'airport_from': str(rs[8]),
				'airport_to': str(rs[9]),
			}
			result.append(obj)
		return result

	def getViagensLongasTempo():
		sql = "SELECT * FROM routes ORDER BY time_flight DESC LIMIT 30;"
		result_db = ConnectorDatabase.runSqlConsulta(sql)
		result = []
		for rs in result_db:
			obj = {
				'id': rs[0],
				'url_mockup': rs[1],
				'distance': str(rs[2]),
				'lowest_price': str(rs[3]),
				'km_price': str(rs[4]),
				'aircraft': rs[5],
				'time_flight': str(rs[6]),
				'average_speed': str(rs[7]),
			}
			result.append(obj)
		return result
