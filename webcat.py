from http.server import BaseHTTPRequestHandler, HTTPServer
from lib import Parser as p

# In order to better understand how this works you can read the http.server python documentation

class RequestHandler(BaseHTTPRequestHandler):

	def do_GET(self): #Handle GET request
		file = ''
		print(self.path)
		if(self.path == '/'): #Serve index.lol
			file = './LOLCODE/index.lol'
		else: #Server other files based on url
			file = "./LOLCODE"+self.path+".lol"
			print(file)
		self.send_response(200)

		# Send headers
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes(p.parse(file), "utf8"))

print('I IZ STARTING')
server_config = ('localhost',8000)
webcat = HTTPServer(server_config,RequestHandler)
print('I IZ SERVIN ON PORT 8000')
print('...')
webcat.serve_forever()