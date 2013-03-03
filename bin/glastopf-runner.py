#!/usr/bin/env python

import sys
import logging
import os
from ConfigParser import ConfigParser
import logging.handlers
from gevent.wsgi import WSGIServer
from glastopf.wsgi_wrapper import GlastopfWSGI

import argparse

from glastopf.glastopf import GlastopfHoneypot


logger = logging.getLogger()

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

    honeypot = GlastopfHoneypot(work_dir=args.workdir)
    honeypot.start_background_workers()
    wsgi_wrapper = GlastopfWSGI(honeypot)

    try:
        WSGIServer((host, port), wsgi_wrapper.application, log=None).serve_forever()
    except KeyboardInterrupt as ex:
        honeypot.stop_background_workers()
