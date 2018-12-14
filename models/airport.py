from .connectorDatabase import ConnectorDatabase

class AirportModel:

	def create(airport):
		sql = "INSERT INTO airports (iata, city, lat, lon, state) VALUES ('"+airport['iata']+"', '"+airport['city']+"', '"+str(airport['lat'])+"', '"+str(airport['lon'])+"', '"+airport['state']+"');"
		ConnectorDatabase.runSql(sql)

	def getEstadosComMaisAeroportos():
		sql = "SELECT DISTINCT(state), COUNT(iata) as total FROM airports GROUP BY state ORDER BY total DESC;"
		result_db = ConnectorDatabase.runSqlConsulta(sql)
		result = []
		for rs in result_db:
			obj = {
				'state': rs[0],
				'total': rs[1]
			}
			result.append(obj)
		return result

	def getAeroportosSaida():
		sql = "SELECT DISTINCT(airport_from) FROM routes"
		result_db = ConnectorDatabase.runSqlConsulta(sql)
		result = []
		for rs in result_db:
			sql_airport_distante = "SELECT airport_to from routes where airport_from = '" + rs[0] + "' ORDER BY distance DESC LIMIT 1"
			result_db_distante = ConnectorDatabase.runSqlConsultaUmElemento(sql_airport_distante)

			sql_airport_proximo = "SELECT airport_to from routes where airport_from = '" + rs[0] + "' ORDER BY distance ASC LIMIT 1"
			result_db_proximo = ConnectorDatabase.runSqlConsultaUmElemento(sql_airport_proximo)

			obj = {
				'iata': rs[0],
				'distante': result_db_distante[0],
				'proximo': result_db_proximo[0]
			}
			result.append(obj)
		return result
