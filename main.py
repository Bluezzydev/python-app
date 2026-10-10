import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

BRANCH = "case/wrong-port"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"branch": BRANCH, "lang": "python", "path": self.path}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = 9999
    print(f"{BRANCH} listening on {port}", flush=True)
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
