#! /usr/bin/python3.6
import psycopg2

try:
    # this:
    print("Iniciando conexão com banco de dados")
    con = psycopg2.connect(host='localhost', database='2xt', user='2xt', password='2xt')
    cur = con.cursor()
    print("Conectado")
    print("\n")

    print("Criando tabela de aeroportos")
    sql_airports = "CREATE TABLE airports (id serial PRIMARY KEY, iata text, city text, lat numeric, lon numeric, state text);"
    cur.execute(sql_airports)
    con.commit()
    print("Tabela criada")
    print("\n")

    print("Criando tabela de rotas")
    sql_routes = "CREATE TABLE routes (id serial PRIMARY KEY, url_mockup text, distance numeric, lowest_price numeric, aircraft text);"
    cur.execute(sql_routes)
    con.commit()
    print("Tabela criada")

    cur.close()
    con.close()
    print("FIM")
    exit()

except psycopg2.Error as e:
    print ("Error !!!!")
    print (e)
    print (e.pgcode)
    print (e.pgerror)
    print (traceback.format_exc())