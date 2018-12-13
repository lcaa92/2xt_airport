#! /usr/bin/python3.6
import psycopg2
from models.connectorDatabase import ConnectorDatabase

try:
    print("Criando tabela de aeroportos")
    sql_airports = "CREATE TABLE airports (id serial PRIMARY KEY, iata text UNIQUE, city text, lat numeric, lon numeric, state text);"
    ConnectorDatabase.runSql(sql_airports)
    print("Tabela criada")

    print("Criando tabela de rotas")
    sql_routes = "CREATE TABLE routes (id serial PRIMARY KEY, url_mockup text, distance numeric, lowest_price numeric, km_price numeric, aircraft text, time_flight numeric, average_speed numeric);"
    ConnectorDatabase.runSql(sql_routes)
    print("Tabela criada")
    print("FIM")

except psycopg2.Error as e:
    print ("Error")
    print (e)
    print (e.pgcode)
    print (e.pgerror)
    print (traceback.format_exc())