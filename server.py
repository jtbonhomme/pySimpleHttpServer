#!/usr/bin/env python
"""
Very simple HTTP server for Python 3.7
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        filename = self.path

        if self.path == '/':
            filename = "index.html"
        else:
            filename = "." + self.path

        try:
            print("open file : " + filename)
            with open(filename, 'r', encoding='utf8') as File:
                content = File.read()
        
            self._set_headers()
            self.wfile.write(content.encode("utf8")) # NOTE: must return a bytes object!

        except:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = "Not Found"
            self.wfile.write(content.encode("utf8")) # NOTE: must return a bytes object!

def run(server_class=HTTPServer, handler_class=requestHandler, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print("Starting httpd server on "+ addr + ":" + str(port))
    httpd.serve_forever()


if __name__ == "__main__":

    run(addr="localhost", port=8000)

