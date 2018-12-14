#! /usr/bin/python3.6
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from models.airport import AirportModel
from models.routes import RouteModel

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == '/viagens_longas_km':
        	arr = RouteModel.getViagensLongasKm()
        	self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/viagens_longas_tempo':
        	arr = RouteModel.getViagensLongasTempo()
        	self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/estado_com_mais_aeroportos':
        	arr = AirportModel.getEstadosComMaisAeroportos()
        	self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        elif self.path == '/aeroportos_saida':
        	arr = AirportModel.getAeroportosSaida()
        	self.wfile.write(bytes(json.dumps(arr), "utf-8"))
        else:
        	self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
