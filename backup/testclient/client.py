import os
from time import sleep
import http.client
import urllib.parse
import urllib.request
params = urllib.parse.urlencode({'testdata1': 1, 'stopServer': 0 })
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

def main():
  i = 0
  conn = http.client.HTTPConnection("server", 8000, timeout=1)  

  while(1):
    sleep(1)
	
	#send request to server 
    print("Sending POST request")
    conn.request("POST", "", params, headers)
    rsp = conn.getresponse()
    print("Response is " + str(rsp.status) + " " + rsp.reason)
    data = rsp.read()
    print(data.decode('utf-8'))
    assert(data.decode('utf-8') == "Valid data received")
    # print(rsp.read().decode())

if __name__ == "__main__":
  main()
