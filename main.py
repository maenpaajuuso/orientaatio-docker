import os
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
name: str = os.environ["NAME"]

content: str = ""

with open("index.html", "r") as file:
    content = file.read()
    content = content.replace("NAME", name)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        byte_content = content.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(byte_content)))
        self.end_headers()

        self.wfile.write(byte_content)

server = HTTPServer(("0.0.0.0", 3030), RequestHandler)
print(f"Listening on localhost:3030")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, stopping...")
    server.server_close()
    print("Server stopped.")
