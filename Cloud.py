#This code performs the operation of sending the data to the cloud by retriving the data from the raspberry-pi

from delimiter import *
import http.client
import urllib.request,urllib.parse,urllib.error
import time
key = "5K4XG9COY42DGYAC"  
a=data[0]
b=data[1]
c=price
def billing():
    while True:
        global a,b,c
        values = {'field1':a,'field2':b,'field3':c,'key':'5K4XG9COY42DGYAC'}
        params = urllib.parse.urlencode(values) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
                billing()
                
