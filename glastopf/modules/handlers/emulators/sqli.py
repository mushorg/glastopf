# Copyright (C) 2012  Lukas Rist
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

import re
import time

from textwrap import dedent

import glastopf.modules.classification.sql as sql
import glastopf.modules.classification.sql_utils.responses as sql_responses
from glastopf.modules.handlers import base_emulator


class SQLiEmulator(base_emulator.BaseEmulator):
    """Emulates a SQL injection vulnerability and a successful attack."""

    def __init__(self, data_dir):
        self.query_cleaner = sql.QueryCleaner()
        self.pre_classifier = sql.PreSQLiClassifier()
        self.query_parser = sql.SQLParser()
        self.query_compare = sql.QueryComparer()
        self.sql_response = sql_responses.SQLResponses()
        super(SQLiEmulator, self).__init__(data_dir)

    def handle(self, attack_event, rule="sql_stmt_list"):
        matched_patterns = []
        payload = []
        for value_list in attack_event.http_request.request_query.values():
            value = value_list[0]
            print value
            if 'CONCAT' in value:
                value = self.query_cleaner.solve_concat(value)
            clean_value = self.query_cleaner._hex_replace(value)
            matched_patterns.extend(
                self.pre_classifier.classify_request(clean_value ))
            self.query_parser.parser_query(clean_value , rule)
            payload.append(clean_value )
        payload = ' '.join(payload)
        #print self.query_parser.tokens
        try:
            if 'FUNCTION_EXPRESSION SLEEP' in self.query_parser.tree.upper():
                parsed_query = self.query_parser.tree
                sleep_time = parsed_query.split("INTEGER_LITERAL ", 1)[1].split(")", 1)[0].strip()
                time.sleep(int(sleep_time))
        except AttributeError:
            pass
        if len(self.query_parser.tokens) > 0:
            best_query, best_ratio = self.query_compare.query_similarity(
                self.query_parser.tokens,
                payload)
            #attack_event.response = self.query_parser.tokens, best_query, best_ratio
        if len(matched_patterns) > 0:
            response = self.sql_response.get_response(matched_patterns[0].response)
            payload_response = re.sub('PAYLOAD',
                                      payload,
                                      response.content)
            attack_event.http_request.set_raw_response(dedent(payload_response))
        else:
            try:
                attack_event.http_request.set_raw_response(dedent(best_query.find("response").text))
            except:
                response = self.sql_response.get_response('mysql_error')
                payload_response = re.sub('PAYLOAD',
                                          payload,
                                          response.content)
                attack_event.http_request.set_raw_response(dedent(payload_response))
