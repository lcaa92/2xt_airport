#! /usr/bin/python3.6
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from models.airport import AirportModel
from models.routes import RouteModel
import string,cgi,time
from os import curdir, sep

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == '/viagens_longas_km':
            self.send_header('Content-type', 'application/json')
            arr = RouteModel.getViagensLongasKm()
            self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/viagens_longas_tempo':
            self.send_header('Content-type', 'application/json')
            arr = RouteModel.getViagensLongasTempo()
            self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/estado_com_mais_aeroportos':
        	arr = AirportModel.getEstadosComMaisAeroportos()
        	self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/aeroportos_saida':
        	arr = AirportModel.getAeroportosSaida()
        	self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        else:
            response_content = open(curdir + sep + "views/dashboard.html")
            #response_content = open("teste.html")
            response_content = response_content.read()
            content_type = "text/html"
            self.send_response(200)
            self.send_header('Content-type', content_type)
            #self.end_headers()
            return self.wfile.write(bytes(response_content, "UTF-8"))
        	#self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        	#self.wfile.write(bytes(response_content, "utf-8"))


httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
