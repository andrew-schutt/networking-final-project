# !/user/bin/python
#-s (sender)

import socket
import sys

#set provided options
host = '127.0.0.1'
port = 4483
#initalize socket variable
s = None

for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, 
                              socket.SOCK_STREAM):
	#get info to create socket
	af, socktype, proto, canonname, sa = res
	try:
		#create new socket
		s = socket.socket(af, socktype, proto)
	#handle error from being unable to create socket
	except socket.error, msg:
		s = None
		continue
	#connect socket to host and port
	try:
		s.connect(sa)
		continue
	except socket.error, msg:
		s.close()
		s = None
		continue
	except:
		break
		
#print generic error message
if s is None:
	print 'could not open socket'
	sys.exit(1)
	
#connection established 
f = open('test.jpg','r') #set to argument
alist = []
while True:
	temp = f.read(4) #byte size
	if temp == "":
		break
	s.send(temp)
	
for x in xrange(0,len(alist)):
	z.write(alist[x])