#!/usr/bin/python3
"""
Main module to create a simple HTTP Server.
"""


from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """
    Class to manage HTTP requests.

    It defines methods to manage GET requests.
    """
    def do_GET(self):
        """
        Treat GET requests.
        Send to correct answer to the correct request.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New-York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data_info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data_info).encode())
        else:
            self.send_error(404, "Endpoint not found")

def run_server(port=8000):
    """
    Run the HTTP server

    Args:
        port: default port: 8000
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPI)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
