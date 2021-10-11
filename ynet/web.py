

import requests
import http.server
import lxml.html
import socketserver
import logging
import sys, os


class Handler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		os.system("python parser.py")
		if self.path == '/':
			self.path = 'index.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(self)


def run():
	server = socketserver.TCPServer(("", 5000), Handler)
	print(f'Starting at {server.server_address}')
	server.serve_forever() # starting the server


if __name__ == '__main__':
	run()
