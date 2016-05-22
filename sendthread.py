import threading
import time

class SendIt(threading.Thread):
	
	def __init__(self, packet, data,  asocket, address, buff, timeout):
		threading.Thread.__init__(self)
		self._packet = packet
		self._asocket = asocket
		self._addr = address
		self._status = True
		self.alist = data		
		self._buff = buff
		self._timeout = timeout/1000

		self.start()
		
		#listen for acks back
		while self._status:	
			ACK, addr = self._asocket.recvfrom(self._buff)
			if ACK == str(self.alist[0]):
				self.setStatus()
				
	def run(self):
		while self._status:
			time.sleep(self._timeout)
			self._asocket.sendto(self._packet, self._addr)

	def setStatus(self):
		self._status = not self._status