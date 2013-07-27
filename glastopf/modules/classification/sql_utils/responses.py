# Copyright (C) 2013  Lukas Rist
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

from xml.etree import ElementTree
import os


class Response(object):
    def __init__(self, r_id, desc, content):
        self.id = r_id
        self.desc = desc
        self.content = content


class SQLResponses(object):
    """ Fetches a response from the list of responses

    The xml file provides a place to store responses.
    """
    # FIXME: Error handling for errors in the xml file
    def __init__(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        responses_file = os.path.join(file_dir, "responses.xml")
        tree = ElementTree.parse(responses_file)
        doc = tree.getroot()
        self.xml_responses = doc.findall("response")

    def _get_responses(self):
        self.responses = []
        for xml_response in self.xml_responses:
            r_id = xml_response.find("id").text.strip()
            desc = xml_response.find("description").text.strip()
            content = xml_response.find("content").text.strip()
            response = Response(r_id, desc, content)
            self.responses.append(response)
        return self.responses

    def get_response(self, r_id):
        for response in self._get_responses():
            if response.id == r_id:
                return response
        for response in self._get_responses():
            if response.id == "mysql_error":
                return response
