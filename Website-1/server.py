import socketserver
import http.server

PORT = 3000
DIRECTORY = "/Users/zakhary/Documents/Claude Workspace/Zak-Website"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass  # silence logs

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server: http://localhost:{PORT}", flush=True)
    httpd.serve_forever()
