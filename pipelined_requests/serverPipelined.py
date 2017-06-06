#!/usr/local/bin/python3

import http.server
import socketserver

postCount=0
headCount=0
getCount=0

def incrementGET():
    global getCount
    getCount += 1
    return

def incrementHEAD():
    global headCount
    headCount += 1
    return

def incrementPOST():
    global postCount
    postCount += 1
    return

class newHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
    	
        incrementGET()
        self.send_response(200)
        reqHeader = self.headers #Takes the headers from the incoming request
        self.send_header(str(reqHeader.keys()), str(reqHeader.values())) #Sends the headers it received back to the client
        self.end_headers()
        print ("This is GET request no.{}".format(getCount))
        print (reqHeader)
        return

    def do_HEAD(self):
    	
    	incrementHEAD()
    	self.send_response(200)
    	head = self.headers
    	self.send_header("TestKey","TestValue")
    	self.end_headers()
    	print ("This is HEAD request no.{}".format(headCount))
    	print (head)
    	return

    def do_POST(self):

    	incrementPOST()
    	self.send_response(200)
    	head2 = self.headers
    	content_len = int(head2.get("Content-Length"))
    	post_body = self.rfile.read(content_len)
    	self.send_header('TestKey', 'TestValue')
    	self.end_headers()
    	print ("This is POST request no.{}".format(postCount))
    	print (head2) #Print the http request's headers
    	#print (post_body) #Print the http request's body
    	return


PORT = 55555

Handler = newHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()