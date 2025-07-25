import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "."

socketserver.TCPServer.allow_reuse_address = True

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Specify your custom start page here
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
