#!/usr/bin/env python

import sys
import logging
import os
from ConfigParser import ConfigParser
import logging.handlers
import argparse
import random

from gevent.wsgi import WSGIServer
import gevent
from OpenSSL import crypto

import glastopf
from glastopf.wsgi_wrapper import GlastopfWSGI
from glastopf.glastopf import GlastopfHoneypot


logger = logging.getLogger()


def setup_logging(logconsole, logfile, verbose, work_dir):
    log_path = os.path.join(work_dir, 'log')
    logger.setLevel(logging.DEBUG)
    if not os.path.isdir(log_path):
        os.mkdir(log_path)

    formatter = logging.Formatter('%(asctime)-15s (%(name)s) %(message)s')
    root_logger = logging.getLogger()
    log_level = logging.DEBUG if verbose else logging.INFO

    if logconsole:
        console_log = logging.StreamHandler()
        console_log.setLevel(log_level)
        console_log.setFormatter(formatter)
        root_logger.addHandler(console_log)

    if logfile:
        logfile = os.path.join(work_dir, logfile)
        file_log = logging.handlers.TimedRotatingFileHandler(
            logfile,
            when="midnight",
            backupCount=31)
        file_log.setLevel(log_level)
        file_log.setFormatter(formatter)
        root_logger.addHandler(file_log)

def start_webserver(workers, host, port, wsgi_wrapper, ssl):
    if ssl:
        server = WSGIServer((host, port), wsgi_wrapper.application, log=None, **ssl)
        logger.info("Glastopf listening on ssl port %d " % port)
    else:
        server = WSGIServer((host, port), wsgi_wrapper.application, log=None)
        logger.info("Glastopf listening on http port %d " % port)
    workers.append(gevent.Greenlet(server.start()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Glastopf runner')
    #defaults to current directory (aka. working directory)
    parser.add_argument('--workdir', dest='workdir', default=os.getcwd())
    parser.add_argument('--prepare', action='store_true', default=False)
    parser.add_argument('--version', action='store_true', default=False,
                        help='Prints version and exits.')
    parser.add_argument('-v', '--verbose', action='store_true', default=False)

    args = parser.parse_args()

    if args.version:
        print 'Glastopf {0}'.format(glastopf.__version__)
        sys.exit(0)

    #prepare directory if workdir/data doesn't exist or if we are asked to do it.
    if args.prepare or not os.path.isdir(os.path.join(args.workdir, 'data/')):
        GlastopfHoneypot.prepare_environment(args.workdir)

    conf_parser = ConfigParser()
    config_file = os.path.join(args.workdir, "glastopf.cfg")
    if not os.path.isfile(config_file):
        sys.exit("Could not find configuration file: glastopf.cfg")
    conf_parser.read(config_file)
    if conf_parser.getboolean("logging", "filelog_enabled"):
        logfile = conf_parser.get("logging", "logfile")
    else:
        logfile = None
    logconsole = conf_parser.getboolean("logging", "consolelog_enabled")
    logger = logging.getLogger()
    setup_logging(logconsole, logfile, args.verbose, args.workdir)

    host = conf_parser.get("webserver", "host")

    ports = []
    if conf_parser.get('webserver', 'port') and conf_parser.get('webserver', 'port') != '':
        ports = map(int, conf_parser.get('webserver', 'port').split(','))
    ssl_ports = []
    if conf_parser.has_option('ssl', 'port') and conf_parser.get('ssl', 'port') != '':
        ssl_ports = map(int, conf_parser.get('ssl', 'port').split(','))


    if conf_parser.get("ssl", "enabled"):
        ssl = {
            'certfile': conf_parser.get("ssl", "certfile"),
            'keyfile': conf_parser.get("ssl", "keyfile"),
            'ciphers': 'AES256',
        }
        # create ssl certificate if none is present.
        if (ssl['certfile']) and (ssl['keyfile']):
            if (not os.path.exists(os.path.join(args.workdir, ssl['certfile']))) \
                    or (not os.path.exists(os.path.join(args.workdir, ssl['certfile']))):
                logger.warning("SSL keys do not exist, creating new ssl keys.")
                client_key = crypto.PKey()
                client_key.generate_key(crypto.TYPE_RSA, 2048)
                client_cert = crypto.X509()
                client_cert.set_version(2)
                client_subj = client_cert.get_subject()
                client_subj.CN = "localhost"
                client_cert.set_serial_number(random.randint(50000000, 100000000))
                client_cert.gmtime_adj_notBefore(0)
                client_cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
                client_cert.set_issuer(client_cert.get_subject())
                client_cert.set_pubkey(client_key)
                client_cert.sign(client_key, 'sha256')

                with open(os.path.join(args.workdir, ssl['certfile']), "wt") as f:
                    f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, client_cert))
                with open(os.path.join(args.workdir, ssl['keyfile']), "wt") as f:
                    f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, client_key))
        else:
            logger.error("Glastopf SSL config broken. Check SSL config section.")

    honeypot = GlastopfHoneypot(work_dir=args.workdir)
    wsgi_wrapper = GlastopfWSGI(honeypot)

    try:
        workers = []

        # dedicated ports from ssl section
        if conf_parser.get("ssl", "enabled") == "True" and len(ssl_ports) > 0:
            # use ports from ssl config selection
            for port in ssl_ports:
                start_webserver(workers, host, port, wsgi_wrapper, ssl)
            # for http use ports from webserver config section
            for port in ports:
                start_webserver(workers, host, port, wsgi_wrapper, False)
        # no dedicated ssl ports, take ports from webserver section and use ssl
        elif conf_parser.get("ssl", "enabled") == "True" and len(ssl_ports) == 0:
            for port in ports:
                start_webserver(workers, host, port, wsgi_wrapper, ssl)
        else:
            # use only ports from webserver config section, no ssl
            for port in ports:
                start_webserver(workers, host, port, wsgi_wrapper, False)

        # start background worker and drop privs
        workers.extend(honeypot.start_background_workers())
        gevent.joinall(workers, raise_error=True)


    except KeyboardInterrupt as ex:
        honeypot.stop_background_workers()
