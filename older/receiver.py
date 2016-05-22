# !/user/bin/python
#-r (reciever)

import socket
import sys

#set provided options
host = None
port = 4483
#initalize socket variable
s = None

for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
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
		s.bind(sa)
		s.listen(1)
		continue
	except:
		break

#print generic error message
if s is None:
	print 'could not open socket'
	sys.exit(1)

#accept connections
conn, addr = s.accept()

#connection established
z = open('output2', 'w') #set to argument
alist = []
while 1:
	data = conn.recv(1024)
	alist.append(data)
	if not data:
		break
	conn.send(data)
print alist
for x in xrange(0, len(alist)):
	z.write(alist[x])
	