import struct
import socket
import hashlib
from ConfigParser import ConfigParser
import json
import logging
import base64
import os

from glastopf.modules.reporting.auxiliary.base_logger import BaseLogger

logger = logging.getLogger(__name__)

"""
Based on Mark Schloessers HPFeed example cli client:
https://raw.github.com/rep/hpfeeds/master/cli/feed.py (9/25/11)
"""

OP_ERROR = 0
OP_INFO = 1
OP_AUTH = 2
OP_PUBLISH = 3


def msghdr(op, data):
    return struct.pack('!iB', 5 + len(data), op) + data


def msgpublish(ident, chan, data):
    if isinstance(data, str):
        data = data.encode('latin1')
    return msghdr(OP_PUBLISH, struct.pack('!B', len(ident)) + ident + struct.pack('!B', len(chan)) + chan + data)


def msgauth(rand, ident, secret):
    hash = hashlib.sha1(rand + secret).digest()
    return msghdr(OP_AUTH, struct.pack('!B', len(ident)) + ident + hash)


class FeedUnpack(object):
    def __init__(self):
        self.buf = bytearray()

    def __iter__(self):
        return self

    def next(self):
        return self.unpack()

    def feed(self, data):
        self.buf.extend(data)

    def unpack(self):
        if len(self.buf) < 5:
            raise StopIteration('No message.')

        ml, opcode = struct.unpack('!iB', buffer(self.buf, 0, 5))
        if len(self.buf) < ml:
            raise StopIteration('No message.')

        data = bytearray(buffer(self.buf, 5, ml - 5))
        del self.buf[:ml]
        return opcode, data


class LogHPFeed(BaseLogger):
    def __init__(self, data_dir, config="glastopf.cfg"):
        self.files_dir = os.path.join(data_dir, 'files/')
        conf_parser = ConfigParser()
        conf_parser.read(config)
        self.options = {
            "enabled": conf_parser.getboolean("hpfeed", "enabled"),
            "host": conf_parser.get("hpfeed", "host"),
            "port": int(conf_parser.getint("hpfeed", "port")),
            "secret": conf_parser.get("hpfeed", "secret").encode('latin1'),
            "chan_events": conf_parser.get("hpfeed", "chan_events").encode('latin1'),
            "chan_files": conf_parser.get("hpfeed", "chan_files").encode('latin1'),
            "ident": conf_parser.get("hpfeed", "ident").encode('latin1').strip(),
        }

        if self.options["enabled"]:
            self.connect()

    def broker_read(self):
        self.unpacker = FeedUnpack()
        data = self.socket.recv(1024)
        while data:
            self.unpacker.feed(data)
            for opcode, data in self.unpacker:
                if opcode == OP_INFO:
                    rest = buffer(data, 0)
                    name, rest = rest[1:1 + ord(rest[0])], buffer(rest, 1 + ord(rest[0]))
                    rand = str(rest)
                    self.socket.send(msgauth(rand, self.options["ident"], self.options["secret"]))
                elif opcode == OP_ERROR:
                    logger.error("Error from server: {0}".format(data))
            try:
                data = self.socket.recv(1024)
            except KeyboardInterrupt:
                break
            except socket.timeout:
                break

    def connect(self):
        logger.info("Connecting to feed broker.")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(3)
        try:
            self.socket.connect((self.options["host"], self.options["port"]))
        except:
            logger.exception("Could not connect to hpfeed broker.")
            self.socket.close()
        else:
            logger.info("Connected to hpfeed broker.")
            self.broker_read()


    #def handle_send(self, channel, data):
    def insert(self, attack_event):

        if attack_event.file_name != None:
            channel = self.options['chan_files']
            with file(os.path.join(self.files_dir, attack_event.file_name), 'r') as file_handler:
                file_content = file_handler.read()
                data = attack_event.file_name + " " + base64.b64encode(file_content)
                self.send_data(channel, data)

        data = json.dumps(attack_event.event_dict())
        channel = self.options['chan_events']
        self.send_data(channel, data)

    def send_data(self, channel, data):
        try:
            self.socket.send(msgpublish(self.options["ident"], channel, data))
        except Exception as e:
            logger.exception("Connection error: {0}".format(e))
            self.connect()
            self.socket.send(msgpublish(self.options["ident"], channel, data))
