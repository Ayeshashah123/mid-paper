import os
from http.server import BaseHTTPRequestHandler, HTTPServer

message = os.getenv("GREETING", "Hello from Python")
port = int(os.getenv("PORT", "8000"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Request received: {self.path}", flush=True)
        self.send_response(200)
        self.end_headers()
        self.wfile.write((message + "\n").encode())

server = HTTPServer(("0.0.0.0", port), Handler)
print(f"Server running on port {port}", flush=True)
server.serve_forever()