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

import json
from lxml import etree

import pylibinjection


class SQLiClassifier(object):

    def __init__(self):
        pass

    def classify(self, string):
        return pylibinjection.detect_sqli(string)


if __name__ == "__main__":
    out = dict()
    sqli_c = SQLiClassifier()
    parser = etree.XMLParser()
    with open("queries.xml", "rb") as fh:
        tree = etree.fromstring(fh.read(), parser)
    i = 0
    for query in tree.xpath("/queries/query"):
        query_str = query.xpath("query")[0].text.strip().encode("UTF-8")
        db = query.xpath("database")[0].text.strip()
        try:
            resp = query.xpath("response")[0].text.strip()
        except IndexError:
            resp = None
        try:
            res = sqli_c.classify(query_str)
            out[i] = {
                "db": db,
                "query": query_str,
                "resp": resp,
                "libinj": res
            }
        except UnicodeEncodeError:
            raise
        else:
            i += 1
    with open("token_map.json", "wb") as fh:
        fh.write(json.dumps(out, indent=4))