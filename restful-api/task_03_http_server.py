"""
This script starts a simple HTTP server using http.server and socketserver.
It handles GET requests for different endpoints and responds accordingly.
"""


import http.server
import socketserver

class simpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler to process GET requests for specific endpoints.
    Args:
        None
    Return:
        None
    """
    def do_GET(self):
        """
        Handle GET requests and return responses based on the requested path.
        Args:
            None
        Return:
            None
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write('{"name": "John", "age": 30, "city": "New York"}')
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("", PORT), simpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
