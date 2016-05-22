from socket import *
from threading import *
import time
import pickle
import hashlib

class Receiver(object):

	def __init__(self, port=6632, output="output", window=20):
		self._wsize = window
		host = ''
		self._port = port
		buff = 1024
		self._output = output
		self._z = open(self._output, "w")
		self._asocket = socket(AF_INET, SOCK_DGRAM)                       
		self._asocket.bind((host, self._port))
		datalist = []
		seqholder = 0
		#create thread method here
		while True:
			#get the packet
			packet, addr = self._asocket.recvfrom(buff)
			#get the list to compute from
			data = pickle.loads(packet)
			#create checksum from data
			m = hashlib.md5()
			m.update(str(data[0])+data[1])
			#check if checksum is equal
			if (m.hexdigest() == data[2] and not
			    datalist.__contains__(data[0:2]) and
			    data[0] > seqholder):
				#extract seqnum and data into datalist
				datalist.append(data[0:2])
				#transmitt seqnum as ACK
				ACK = str(data[0])
				self._asocket.sendto(ACK, addr)
				datalist.sort()
				for x in range(0, len(datalist)):
					self._z.write(datalist[x][1])
				seqholder = data[0]
				datalist = []
			if not data[1]:
				print "closing..."
				break
		self._asocket.close()