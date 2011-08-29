
import sys
import logging
import random
import struct
logging.basicConfig(level=logging.DEBUG)

from evnet import loop, unloop, listenplain
from evnet.util import EventGen
from evnet.promise import Promise

# WebSocket based on Mark Schloessers example.

class WebSockListener(EventGen):
	def __init__(self, port):
		EventGen.__init__(self)

		self.l = listenplain(host='0.0.0.0', port=port)
		self.l._on('connection', self.connection)

	def connection(self, c, addr):
		print 'cli', addr,
		self._event('connection', WebSock(c, addr))

class WebSock(EventGen):
	def __init__(self, c, addr):
		EventGen.__init__(self)
		self.c, self.addr = c, addr
	
		self.c._on('ready', self.ready)
		self.c._on('close', self.closed)
		self.c._on('read', self.read)

	def ready(self):
		self._event('ready')

	def closed(self, e):
		self._event('close', e)

	def read(self, d):
		print 'read', repr(d)


if __name__ == '__main__':
	a = WebSockListener(int(sys.argv[2]))

	def new_conn(c):
		def onready():
			def dbgprint(r):
				print 'dbgprint', r

		def closed(e):
			pass
			#print e

		c._on('ready', onready)
		c._on('close', closed)

	a._on('connection', new_conn)

	loop()