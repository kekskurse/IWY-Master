import socket

class FreeColor:
	def __init__(self):
		self.blubs = {}
	def addStripe(self, ipaddr, name):
		entry = {name: ipaddr}
		self.blubs.update(entry)
	def changeColor(self, blubName, red, green, blue, h):
		#ops = self.createByte([0x56, red, green, blue, 0x00, 0xf0, 0xaa])
		ops = self.createByte([0x9d, 0x62, 0x00, 0x00, 0x00, 0x01, h, red, green, blue, 0x00, 0x00, 0xf0, 0x00, 0xf0, 0xc0, 0x10, 0x10, 0x10, 0x0d])
		ip = self.blubs[blubName]
		self.send(ip, ops)
	def on(self, blubName):
		self.changeColor(blubName, 0xff, 0xff, 0xff, 0xff)
	def off(self, blubName):
		self.changeColor(blubName, 0x00, 0x00, 0x00, 0x00)
	def createByte(self, paramlist):
		#Python 3:
		return bytes(paramlist)
		#Python 2:
		return ''.join(chr(x) for x in paramlist)
	def send(self, ip, ops):
		print("Send to Blub")
		print(ip)
		print(ops)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((ip,5000))
		s.send(ops)
		s.close()