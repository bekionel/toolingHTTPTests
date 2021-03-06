#!/usr/local/bin/python3

import xml.etree.ElementTree as ET
import http.client
import argparse

parser = argparse.ArgumentParser(description = 'Set the address and port to connect to')
parser.add_argument('-a', required = True,type = str, help = 'Specify the desired IP address')
parser.add_argument('-p', type = int, required = True , help = 'Specify the desired port number')
args = parser.parse_args()

#Establish connection with the server
conn = http.client.HTTPConnection(args.a, port=args.p)

#Create a single parent element with a hundred children
first = ET.Element('root')
for x in range(1,101):
	k = ET.SubElement(first, 'item')
	k.text = str(x)

#Create a string containing the xml elements to be sent
package_to_send = ET.tostring(first)
#print (package_to_send)

#Send the http request with the xml elements
for x in range(1,4):
    print ("Sending request no{}".format(x))
    req = conn.request("POST", "/", package_to_send, {"Connection": "Keep-Alive"})

#Get the response from the server
    response = conn.getresponse()
#print (response.getheaders()) #Prints all the headers in two separate lists
    re = response.msg 
    print (re) #Prints the headers in corresponding key: value pairs