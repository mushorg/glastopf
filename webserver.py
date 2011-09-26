import sys
import logging
logging.basicConfig(level=logging.DEBUG)
from ConfigParser import ConfigParser

from evnet import loop, unloop, listenplain
from evnet.util import EventGen
from evnet.promise import Promise

import glastopf

# WebSocketListener based on Mark Schloessers evnet example https://github.com/rep/evnet

class WebSockListener(EventGen):
    def __init__(self):
        EventGen.__init__(self)
        self.glastopf_honeypot = glastopf.GlastopfHoneypot()
        conf_parser = ConfigParser()
        conf_parser.read("glastopf.cfg")
        host = conf_parser.get("webserver", "host")
        port = conf_parser.getint("webserver", "port")
        try:
            self.l = listenplain(host=host, port=port)
        except Exception, e:
            print "\nUnable to bind socket:",
            if e.errno == 13:
                print "Permission denied. Run as root!\n"
            if e.errno == 98:
                print "Port " + str(port) + " already bound. Stop running service on port " + str(port) + " first.\n"
            else:
                print "[ Errno " + str(e.errno) + "]", e.strerror + "\n"
            sys.exit(1)
        else:
            print "Webserver running on:", host + ":" + str(port), "waiting for connections...\n"
            self.l._on('connection', self.connection)

    def connection(self, c, addr):
        self._event('connection', WebSock(c, addr, self.glastopf_honeypot))

class WebSock(EventGen):
    def __init__(self, c, addr, glastopf):
        EventGen.__init__(self)
        self.glastopf_honeypot = glastopf
        self.c, self.addr = c, addr
    
        self.c._on('ready', self.ready)
        self.c._on('close', self.closed)
        self.c._on('read', self.read)

    def ready(self):
        self._event('ready')

    def closed(self, e):
        self._event('close', e)

    def read(self, d):
        #print 'read', repr(d)
        response = self.glastopf_honeypot.handle_request(d, self.addr)
        self.send(response)
        self.c.close()
        
    def send(self, s):
        self.c.write(s)

if __name__ == '__main__':
    a = WebSockListener()
    
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