#This code reads the RFID tags and prints the values

from Read1 import *
import re

#def bill():
pattern='[0-9]'
detail=text
data=detail.split(" ")
print(data[0])
print(data[1])
result=re.findall(pattern,data[1])
price=''.join(result)
print(price)

