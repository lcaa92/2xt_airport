import psycopg2

class ConnectorDatabase:


	def runSql(sql):
		try:
			con = psycopg2.connect(host='localhost', database='2xt', user='2xt', password='2xt')
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