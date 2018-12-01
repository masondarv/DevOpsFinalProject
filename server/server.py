import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class serv(BaseHTTPRequestHandler):
  def do_GET(self):
    print("Got GET request")
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    print("Sending response")
    self.wfile.write(os.environ['HW2MSG'].encode())

def main():
  addr = ('', 5000)
  httpd = HTTPServer(addr, serv)

  print("Starting server")
  httpd.serve_forever()

if __name__ == "__main__":
  main()
