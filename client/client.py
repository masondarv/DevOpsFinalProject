import os
from time import sleep
import http.client

def main():
  i = 0
  conn = http.client.HTTPConnection("server", 5000, timeout=1)  

  while(1):
    print("Client is sleeping for " + os.environ['HW2INT'] + " ms")
    sleep(float(os.environ['HW2INT']) / 1000.0)
    print("Sending GET request")

    conn.request("GET", "/")
    rsp = conn.getresponse()
    print("Response is " + str(rsp.status) + " " + rsp.reason)
    print(rsp.read().decode())

if __name__ == "__main__":
  main()
