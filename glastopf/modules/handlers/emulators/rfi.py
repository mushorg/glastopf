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

import glastopf.sandbox.sandbox as sandbox
from glastopf.modules.handlers import base_emulator

logger = logging.getLogger(__name__)


class RFIEmulator(base_emulator.BaseEmulator):
    def __init__(self, data_dir):
        super(RFIEmulator, self).__init__(data_dir)
        self.downloaded_file_exists = False
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
        file_sha256 = hashlib.sha256(injected_file).hexdigest()
        return file_name, file_sha256

    def store_file(self, injected_file):
        file_name, file_sha256 = self.get_filename(injected_file)
        if not os.path.exists(os.path.join(self.files_dir, file_name)):
            with open(os.path.join(self.files_dir, file_name), 'w+') as local_file:
                local_file.write(injected_file)
        else:
            self.downloaded_file_exists = True
        return file_name, file_sha256

    def download_file(self, url):
        injectd_url = self.extract_url(urllib2.unquote(url))
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
            file_name, file_sha256 = self.store_file(injected_file)
        return file_name, file_sha256

    def handle(self, attack_event):
        if attack_event.http_request.command == 'GET':
            attack_event.file_name, attack_event.file_sha256  = self.download_file(
                attack_event.http_request.path)
        elif attack_event.http_request.command == 'POST':
            pass
        else:
            logger.error("Unsupported method: {0}".format(attack_event.http_request.command))
        if attack_event.file_name:
            response = sandbox.run(attack_event.file_name, self.data_dir)
            attack_event.http_request.set_raw_response(response)
        attack_event.known_file = self.downloaded_file_exists
        return attack_event
