from socket import *
from sendthread import *
import pickle
import hashlib

class Sender(object):
	
	def __init__(self, host, port, aninput, window, payload = 8, timeout = 5):
		self._wsize = window
		self._ip = host
		self._port = port
		buff = 1024
		self._input = aninput
		self._f = open(self._input, "r")
		self._payload = payload
		self._timeout = timeout
		self._asocket = socket(AF_INET, SOCK_DGRAM)
		address = (self._ip, self._port)
		seqnum = 0
		wlist = []
		#create thread method here
		while True:
			#begin packet crafting
			alist = []
			#generate linear sequence num.
			seqnum = seqnum + 1
			alist.append(seqnum)
			#read in data
			data = self._f.read(self._payload)
			alist.append(data)
			#create checksum
			m = hashlib.md5()
			m.update(str(seqnum)+data)
			m = m.hexdigest()
			alist.append(m)
			#pack into packet! (turn into string)
			packet = pickle.dumps(alist)
			#normal progression and sending
			send = SendIt(packet, alist, self._asocket,
			              address, buff, self._timeout)
			print data
			#check if windowsize has been met
			if (len(wlist) == window):
				i = 0
				while (len(wlist) == self._wsize):
					if wlist[i]._status == False:
						wlist.pop(i)
					elif (i == len(wlist)):
						i = 0
					else:
						i = i + 1
			#check if last packet
			elif data == "":
				send = SendIt(packet, alist, self._asocket, address, buff, 5)
				break
			else:
				wlist.append(send)	

		self._asocket.close()