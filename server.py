import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000
DIRECTORY = "/Users/bensmith/Desktop/tiika"

class RewriteHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        # Get the requested path
        path = self.translate_path(self.path)
        
        # If path doesn't exist and doesn't end in .html, try adding .html
        if not os.path.exists(path) and not self.path.endswith('.html'):
            # Remove query string if present
            clean_path = self.path.split('?')[0]
            html_path = self.translate_path(clean_path + '.html')
            
            if os.path.exists(html_path):
                # Rewrite the path to include .html
                self.path = clean_path + '.html'
        
        # Call the parent class to handle the request normally
        return super().do_GET()

with socketserver.TCPServer(("", PORT), RewriteHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Directory: {DIRECTORY}")
    httpd.serve_forever()