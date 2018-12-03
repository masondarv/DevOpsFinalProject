import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class server(BaseHTTPRequestHandler):

  stopped = False
  
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
	
	
  def do_POST(self):
    print("Got POST request")
	## send response header to client
    self._set_headers()
	
	## extract contents of http request body
    content_len = int(self.headers.get('content-length', 0))
    post_body = self.rfile.read(content_len)
    print(post_body);
	
	## parse out individual fields of http request body
    fields = parse_qs(post_body)
    print(fields);
	
	## evaluate received data to determine if it is within valid range
    if int(fields[b'testdata1'][0].decode('utf-8')) > 10 and int(fields[b'testdata1'][0].decode('utf-8')) <20:
      message = "Valid data received"
	  
    else:
      message = "Invalid data received"
    print("Received data")
    print(fields[b'testdata1'][0].decode('utf-8'))

    self.wfile.write(message.encode('utf-8'))
	
    if int(fields[b'stopServer'][0].decode('utf-8'))
    stopped = True

	

def main():
  addr = ('', 8000)
  httpd = HTTPServer(addr, server)

  print("Starting server")
  httpd.serve_forever()
  
  while(1)
    if http.stopped = True
    http.server_close()
	  

if __name__ == "__main__":
  main()
