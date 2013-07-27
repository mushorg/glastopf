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

import difflib
import os
import json

import pylibinjection


class SQLiClassifier(object):
    """ Compares input to known queries

    Compares the input query with a set of known queries.
    Goal is to select a proper response, not to decide if malicious.
    """
    def __init__(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        queries_file = os.path.join(file_dir, "sql_utils", "token_map.json")
        with open(queries_file, "rb") as fh:
            self.token_map = json.load(fh)

    def classify(self, string):
        return pylibinjection.detect_sqli(string)

    def _token_squence_matcher(self, query_tokens):
        """ Compares the token squence

        Libinjection tokenizes the query. We compare those tokens with our known list.
        """
        best_ratio = 0.0
        best_query = None
        for i, val in self.token_map.items():
            # Sequence comparison
            ratio = difflib.SequenceMatcher(None, query_tokens, val["libinj"]["tokens"]).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_query = i
            if best_ratio == 1.0:
                break
        return best_query, best_ratio

    def _query_string_match(self, payload):
        """ Compares the query string

        Compares the query string with our known list.
        This is usually less successful than the token comparison but catches corner cases.
        """
        ratio = 0.8
        queries = [query["query"].lower() for query in self.token_map.values()]
        best_matches = difflib.get_close_matches(payload, queries, 1, ratio)
        if len(best_matches) > 0:
            for i, val in self.token_map.items():
                if val["query"].lower() == best_matches[0]:
                    return i, ratio
        return None, None

    def query_similarity(self, query_tokens, payload):
        best_query, best_ratio = self._query_string_match(payload)
        if best_query is None:
            best_query, best_ratio = self._token_squence_matcher(query_tokens)
        return best_query, best_ratio


if __name__ == "__main__":
    sqli_c = SQLiClassifier()
    query = "anything' OR 'x'='x';"
    data = sqli_c.classify(query)
    print data
    best_query, best_ratio = sqli_c.query_similarity(data["fingerprint"], query.lower())
    print sqli_c.token_map[best_query], best_ratio
