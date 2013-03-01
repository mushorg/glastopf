import sys
import logging
import os
from ConfigParser import ConfigParser
import logging.handlers
import shutil
import pkgutil
import argparse

from evnet import loop, unloop, listenplain
from evnet.util import EventGen
from evnet.promise import Promise
from glastopf.glastopf import GlastopfHoneypot


logger = logging.getLogger()

# WebSocketListener based on Mark Schloessers evnet 
# example https://github.com/rep/evnet


class WebSockListener(EventGen):
    def __init__(self, host, port, workdir):
        EventGen.__init__(self)
        try:
            self.l = listenplain(host=host, port=port)
        except Exception, e:
            if e.errno == 13:
                info = "Permission denied. Run as root!"
            if e.errno == 98:
                info = "Port " + str(port) + " already bound. Stop running service on port " + str(port) + " first."
            else:
                info = "[ Errno " + str(e.errno) + "]", e.strerror
            logger.exception("Unable to bind socket: {0}".format(info))
            sys.exit(1)
        else:
            logger.info("Webserver running on: {0}:{1} waiting for connections.".format(host, str(port)))
            self.l._on('connection', self.connection)
            self.glastopf_honeypot = GlastopfHoneypot(work_dir=workdir)
            self.glastopf_honeypot.start_background_workers()

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
        self.c._on('allsent', self.close)

    def ready(self):
        self._event('ready')

    def closed(self, e):
        self._event('close', e)

    def read(self, d):
        #print 'read', repr(d)
        response = self.glastopf_honeypot.handle_request(d, self.addr, self.c)
        self.send(response)

    def send(self, s):
        self.c.write(s)

    def close(self):
        self.c.close()


def setup_logging(logconsole, logfile):
    logger.setLevel(logging.DEBUG)
    if not os.path.isdir('log'):
        os.mkdir('log')

    formatter = logging.Formatter('%(asctime)-15s (%(name)s) %(message)s')
    root_logger = logging.getLogger()

    if logconsole:
        console_log = logging.StreamHandler()
        console_log.setLevel(logging.DEBUG)
        console_log.setFormatter(formatter)
        root_logger.addHandler(console_log)

    if logfile != None:
        file_log = logging.handlers.TimedRotatingFileHandler(
            logfile,
            when="midnight",
            backupCount=31)
        file_log.setLevel(logging.DEBUG)
        file_log.setFormatter(formatter)
        root_logger.addHandler(file_log)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Glastopf runner')
    #defaults to current directory (aka. working directory)
    parser.add_argument('--workdir', dest='workdir', default=os.getcwd())
    parser.add_argument('--prepare', action='store_true', default=False)

    args = parser.parse_args()

    #prepare directory if workdir directory contains no files or if we are asked to do it.
    if args.prepare or len(os.listdir(args.workdir)) == 0:
        GlastopfHoneypot.prepare_environment(args.workdir)

    conf_parser = ConfigParser()
    if not os.path.isfile("glastopf.cfg"):
        sys.exit("Could not find configuration file: glastopf.cfg")
    conf_parser.read("glastopf.cfg")
    if conf_parser.getboolean("logging", "filelog_enabled"):
        logfile = conf_parser.get("logging", "logfile")
    else:
        logfile = None
    logconsole = conf_parser.getboolean("logging", "consolelog_enabled")
    logger = logging.getLogger()
    setup_logging(logconsole, logfile)

    host = conf_parser.get("webserver", "host")
    port = conf_parser.getint("webserver", "port")
    a = WebSockListener(host, port, args.workdir)

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

    try:
        loop()
    except KeyboardInterrupt as ex:
        glastopf = a.glastopf_honeypot
        glastopf.stop_background_workers()
