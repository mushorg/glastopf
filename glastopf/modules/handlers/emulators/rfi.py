# Copyright (C) 2015 Lukas Rist
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import urllib2
import hashlib
import os
import re
import logging
import ssl
import socket
import requests
from urlparse import urlparse
from socket import inet_aton
from struct import unpack
from requests.utils import requote_uri



import glastopf.sandbox.sandbox as sandbox
from glastopf.modules.handlers import base_emulator

logger = logging.getLogger(__name__)

def check_ssrf(url):
    hostname = urlparse(url).hostname

    def ip2long(ip_addr):
        return unpack("!L", inet_aton(ip_addr))[0]

    def is_inner_ipaddress(ip):
        ip = ip2long(ip)
        return ip2long('127.0.0.0') >> 24 == ip >> 24 or \
                ip2long('10.0.0.0') >> 24 == ip >> 24 or \
                ip2long('172.16.0.0') >> 20 == ip >> 20 or \
                ip2long('192.168.0.0') >> 16 == ip >> 16

    try:
    	# print re.match(r"^http(s)?://(.*?)$", url)
        # if not re.match(r"^https?://.*/.*$", url):
        if not re.match(r"^http(s)?://(.*?)$", url):
            raise BaseException("url format error")
        # print socket.getaddrinfo(hostname, 'http')
        ip_address = socket.getaddrinfo(hostname, 'http')[0][4][0]
        logger.info(ip_address)
        if is_inner_ipaddress(ip_address):
            raise BaseException("inner ip address attack")
        return True, "success"
    except BaseException as e:
        return False, str(e)
    except:
        return False, "unknow error"

def safe_request_url(url, **kwargs):
    success, errstr = check_ssrf(url)
    if not success:
        raise requests.exceptions.InvalidURL("SSRF Attack: %s" % (errstr,))
    return requests.get(url, **kwargs)


class RFIEmulator(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(RFIEmulator, self).__init__(data_dir)
        self.files_dir = os.path.join(self.data_dir, 'files/')
        if not os.path.exists(self.files_dir):
            os.mkdir(self.files_dir)

    @classmethod
    def extract_url(cls, url):
        protocol_pattern = re.compile("=.*(http(s)?|ftp(s)?)", re.IGNORECASE)
        matched_protocol = protocol_pattern.search(url).group(1)
        # FIXME: Check if the extracted url is actually a url
        injected_url = matched_protocol + url.partition(matched_protocol)[2].split("?")[0]
        return injected_url.strip("=")

    @classmethod
    def get_filename(cls, injected_file):
        file_name = hashlib.md5(injected_file).hexdigest()
        return file_name

    def store_file(self, injected_file):
        file_name = self.get_filename(injected_file)
        if not os.path.exists(os.path.join(self.files_dir, file_name)):
            with open(os.path.join(self.files_dir, file_name), 'w+') as local_file:
                local_file.write(injected_file)
        return file_name
    
    def download_file(self, url):
        injectd_url = self.extract_url(urllib2.unquote(url))
        try:
            r = safe_request_url(injectd_url)
        except Exception as e:
            logger.info(e)
            file_name = None 
            return file_name
        try:
            req = urllib2.Request(injectd_url)
            # Set User-Agent to look more credible
            req.add_unredirected_header('User-Agent', '-')
            # FIXME: We need a timeout on read here
            injected_file = urllib2.urlopen(req, timeout=4).read()
            #  If the file is hosted on a SSL enabled host get the certificate
            if re.match('^https', injectd_url, re.IGNORECASE):
                proto, rest = urllib2.splittype(injectd_url)
                host, rest = urllib2.splithost(rest)
                host, port = urllib2.splitport(host)
                if port is None:
                    port = 443

                cert_file = ssl.get_server_certificate((host, int(port)))
                cert_name = self.store_file(cert_file)

        except IOError as e:
            logger.exception("Failed to fetch injected file, I/O error: {0}".format(e))
            # TODO: We want to handle the case where we can't download
            # the injected file but pretend to be vulnerable.
            file_name = None
        else:
            file_name = self.store_file(injected_file)
        return file_name

    def handle(self, attack_event):
        if attack_event.http_request.command == 'GET':
            #pass
            attack_event.file_name = self.download_file(
                attack_event.http_request.path)
        elif attack_event.http_request.command == 'POST':
            pass
        else:
            logger.error("Unsupported method: {0}".format(attack_event.http_request.command))
        if attack_event.file_name:
            response = sandbox.run(attack_event.file_name, self.data_dir)
            attack_event.http_request.set_raw_response(response)
        return attack_event
