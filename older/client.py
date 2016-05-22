# !/user/bin/python
#Author:		Andrew Schutt
#Created:		11/6/10
#Update:		11/7/10

#simple client (reciever)

import socket
import sys

host = '134.161.47.23'
port = 4483
s = None
for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
	af, socktype, proto, canonnname, sa = res
	try:
		s = socket.socket(af, socktype, proto)
	except socket.error, msg:
		s = None
		continue
	try:
		s.connect(sa)
	except socket.error, msg:
		s.close()
		s = None
		continue
	break
if s is None:
	print 'could not open socket'
	
f = open('test.jpg', 'r')
alist = []
while(True):
	temp = f.read(4)
	if temp == "":
		break
	s.send(temp)
data = s.recv(1024)
s.close()
print 'Received', repr(data)