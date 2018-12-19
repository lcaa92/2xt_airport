import psycopg2
from config.config import Config
import traceback

class ConnectorDatabase:

	def runSql(sql):
		try:
			con = psycopg2.connect(host=Config.database['host'], database=Config.database['database'], user=Config.database['user'], password=Config.database['password'])
			cur = con.cursor()

			cur = con.cursor()
			cur.execute(sql)
			con.commit()

			cur.close()
			con.close()

		except psycopg2.Error as e:
			print ("Error")
			print (e)
			print (e.pgcode)
			print (e.pgerror)
			print (traceback.format_exc())

	def runSqlConsulta(sql):
		try:
			con = psycopg2.connect(host=Config.database['host'], database=Config.database['database'], user=Config.database['user'], password=Config.database['password'])
			cur = con.cursor()

			cur = con.cursor()
			cur.execute(sql)
			result=cur.fetchall();
			con.commit()

			cur.close()
			con.close()
			return result
		except psycopg2.Error as e:
			print ("Error")
			print (e)
			print (e.pgcode)
			print (e.pgerror)
			print (traceback.format_exc()) 

	def runSqlConsultaUmElemento(sql):
		try:
			con = psycopg2.connect(host=Config.database['host'], database=Config.database['database'], user=Config.database['user'], password=Config.database['password'])
			cur = con.cursor()

			cur = con.cursor()
			cur.execute(sql)
			result=cur.fetchone();
			con.commit()
			
			cur.close()
			con.close()
			return result
		except psycopg2.Error as e:
			print ("Error")
			print (e)
			print (e.pgcode)
			print (e.pgerror)
			print (traceback.format_exc()) 