# Copyright (C) 2015 Johnny Vestergaard <jkv@unixcluster.dk>
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

import unittest
import os
import shutil
import tempfile
import hashlib

from StringIO import StringIO

from ConfigParser import ConfigParser

from glastopf.modules.reporting.auxiliary.stix.stix_transform import StixTransformer
from glastopf.modules.reporting.auxiliary.log_taxii import TaxiiLogger
from glastopf.testing.mitre_stix_validator import STIXValidator
from glastopf.modules.HTTP.handler import HTTPHandler
from glastopf.modules.events.attack import AttackEvent


class Test_Stix(unittest.TestCase):

    def setUp(self):
        self.config = ConfigParser()
        self.config.add_section('taxii')
        self.config.set('taxii', 'enabled', "True")
        self.config.set('taxii', 'include_contact_info', "True")
        self.config.set('taxii', 'contact_name', 'James Bond')
        self.config.set('taxii', 'contact_email', 'a@b.c')
        self.config.set('taxii', 'host', 'taxiitest.mitre.org')
        self.config.set('taxii', 'port', '80')
        self.config.set('taxii', 'inbox_path', '/services/inbox/default/')
        self.config.set('taxii', 'use_auth_basic', 'False')
        self.config.set('taxii', 'auth_basic_username', 'your_username')
        self.config.set('taxii', 'auth_basic_password', 'your_password')
        self.config.set('taxii', 'use_auth_certificate', 'False')
        self.config.set('taxii', 'auth_certificate_keyfile', 'keyfile_oath')
        self.config.set('taxii', 'auth_certificate_certfile', 'certfile_path')
        self.config.set('taxii', 'use_https', 'True')




        self.tmpdir = tempfile.mkdtemp()
        self.files_dir = os.path.join(self.tmpdir, 'files')
        os.mkdir(self.files_dir)
        self.stix_transformer = StixTransformer(self.config, self.tmpdir)
        self.xml_validator = STIXValidator(None, True, False)

    def tearDown(self):
        if os.path.isdir(self.tmpdir):
            shutil.rmtree(self.tmpdir)

    def test_stix_transform(self):
        """
        Objective: Test if the expected XML is generated from a "unknown" attack event.
        """

        test_event = AttackEvent()
        test_event.source_addr = ('1.2.3.4', 43811)
        http_request_content = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        test_event.http_request = HTTPHandler(http_request_content, None, server_version="", sys_version="")
        stix_package_xml = self.stix_transformer.transform(test_event)

        (isvalid, validation_error, best_practice_warnings) = self.xml_validator.validate(StringIO(stix_package_xml.encode('utf-8')))
        self.assertTrue(isvalid, 'Error while parsing STIX xml: {0}'.format(validation_error))
        self.assertTrue('<HTTPSessionObj:User_Agent>test</HTTPSessionObj:User_Agent>' in stix_package_xml)
        self.assertTrue('<HTTPSessionObj:HTTP_Method datatype="string">GET</HTTPSessionObj:HTTP_Method>' in stix_package_xml)
        self.assertTrue('<HTTPSessionObj:Value>/test</HTTPSessionObj:Value>' in stix_package_xml)
        self.assertTrue('<HTTPSessionObj:Version>HTTP/1.0</HTTPSessionObj:Version>' in stix_package_xml)

    def test_stix_transform_invalid_header(self):
        """
        Objective: Test if we can generate valid XML from a HTTP request with a invalid header item.
        """

        test_event = AttackEvent()
        test_event.source_addr = ('1.2.3.4', 43811)
        http_request_content = """GET /test HTTP/1.0\r\nXUser-XAgent: test\r\n\r\n"""
        test_event.http_request = HTTPHandler(http_request_content, None, server_version="", sys_version="")
        stix_package_xml = self.stix_transformer.transform(test_event)

        (isvalid, validation_error, best_practice_warnings) = self.xml_validator.validate(StringIO(stix_package_xml.encode('utf-8')))
        self.assertTrue(isvalid, 'Error while parsing STIX xml: {0}'.format(validation_error))
        #TODO: Parse XML and check content of header, request_line, etc.

    def test_stix_transform_event_with_rfidata(self):
        """
        Objective: Test if the expected XML is generated from a "unknown" attack event.
        """

        rfi_data = """<?php echo "<script>alert("test");</script>";?>"""
        rfi_md5 = hashlib.md5(rfi_data).hexdigest()
        with open(os.path.join(self.files_dir, rfi_md5), 'w') as rfi_file:
            rfi_file.writelines(rfi_data)

        test_event = AttackEvent()
        test_event.source_addr = ('1.2.3.4', 43811)
        test_event.matched_pattern = 'rfi'
        test_event.file_name = rfi_md5
        http_request_content = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        test_event.http_request = HTTPHandler(http_request_content, None, server_version="", sys_version="")
        stix_package_xml = self.stix_transformer.transform(test_event)
        (isvalid, validation_error, best_practice_warnings) = self.xml_validator.validate(StringIO(stix_package_xml.encode('utf-8')))
        self.assertTrue(isvalid, 'Error while parsing STIX xml: {0}'.format(validation_error))
        self.assertTrue('<cyboxCommon:Simple_Hash_Value>0e209064ee6949f6e57b3d77d5b1f92c</cyboxCommon:Simple_Hash_Value>' in stix_package_xml)
        self.assertTrue('<cyboxCommon:Simple_Hash_Value>11a2a92d391f10821dbb90f1f7e6ae0f2374231e0ccd611665c95d6d7a3bb43c</cyboxCommon:Simple_Hash_Value>' in stix_package_xml)
        self.assertTrue('<ArtifactObj:Raw_Artifact datatype="string"><![CDATA[PD9waHAgZWNobyAiPHNjcmlwdD5hbGVydCgidGVzdCIpOzwvc2NyaXB0PiI7Pz4=]]></ArtifactObj:Raw_Artifact>' in stix_package_xml)

    @unittest.skip('disabled until stix server up and running again')
    def test_taxii_connectivity(self):
        """
        Objective: Test if we can send a message to mitre's test TAXII server.
        """
        self.config.set('taxii', 'use_https', 'False')
        config_file = tempfile.mkstemp()[1]
        with open(config_file, 'w') as f:
            self.config.write(f)
        test_event = AttackEvent()
        test_event.source_addr = ('1.2.3.4', 43811)
        http_request_content = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        test_event.http_request = HTTPHandler(http_request_content, None, server_version="", sys_version="")

        taxiiLogger = TaxiiLogger(self.tmpdir, os.getcwd(), config_file)
        taxii_result = taxiiLogger.insert(test_event)
        # TaxiiLogger returns false if the message could not be delivered
        self.assertTrue(taxii_result)
        f.close() #clean the tempfile

    @unittest.skip('disabled until stix server up and running again')
    def test_taxii_connectivity_https(self):
        """
        Objective: Test if we can send a message to mitre's test TAXII server using https.
        """
        self.config.set('taxii', 'use_https', 'True')
        config_file = tempfile.mkstemp()[1]
        with open(config_file, 'w') as f:
            self.config.write(f)
        test_event = AttackEvent()
        test_event.source_addr = ('1.2.3.4', 43811)
        http_request_content = """GET /test HTTP/1.0\r\nUser-Agent: test\r\n\r\n"""
        test_event.http_request = HTTPHandler(http_request_content, None, server_version="", sys_version="")

        taxiiLogger = TaxiiLogger(self.tmpdir, os.getcwd(), config_file)
        taxii_result = taxiiLogger.insert(test_event)
        # TaxiiLogger returns false if the message could not be delivered
        self.assertTrue(taxii_result)
        f.close() #clean the tempfile


if __name__ == '__main__':
    unittest.main()
