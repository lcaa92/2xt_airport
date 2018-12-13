from .connectorDatabase import ConnectorDatabase

class AirportModel:

	def create(airport):
		sql = "INSERT INTO airports (iata, city, lat, lon, state) VALUES ('"+airport['iata']+"', '"+airport['city']+"', '"+str(airport['lat'])+"', '"+str(airport['lon'])+"', '"+airport['state']+"');"
		ConnectorDatabase.runSql(sql)
