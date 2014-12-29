import socket

class IWYMaster:
	def __init__(self):
		self.blubs = {}
	def addBlub(self, ipaddr, name):
		entry = {name: ipaddr}
		self.blubs.update(entry)
	def changeColor(self, blubName, red, green, blue):
		ops = self.createByte([0x56, red, green, blue, 0x00, 0xf0, 0xaa])
		ip = self.blubs[blubName]
		self.send(ip, ops)
	def setWarmWidth(self, blubName, width = 0xff):
		ops = self.createByte([0x56, 0x00, 0x00, 0x00, width, 0x0f, 0xaa])
		ip = self.blubs[blubName]
		self.send(ip, ops)
	def on(self, blubName):
		ops = self.createByte([0xcc, 0x23, 0x33])
		ip = self.blubs[blubName]
		self.send(ip, ops)
	def off(self, blubName):
		ops = self.createByte([0xcc, 0x24, 0x33])
		ip = self.blubs[blubName]
		self.send(ip, ops)
	def createByte(self, paramlist):
		#Python 3:
		#return bytes(paramlist)
		#Python 2:
		return ''.join(chr(x) for x in paramlist)
	def send(self, ip, ops):
		print("Send to Blub")
		print(ip)
		print(ops)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((ip,5577))
		s.send(ops)
		s.close()