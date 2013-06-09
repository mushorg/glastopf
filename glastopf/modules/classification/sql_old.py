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

import difflib
import urllib
import re
import binascii
import os

from xml.dom.minidom import parse
from xml.etree import ElementTree

import antlr3
from glastopf.modules.classification.sql_utils.SQLiteLexer import SQLiteLexer
from glastopf.modules.classification.sql_utils.SQLiteParser import SQLiteParser


class Pattern(object):
    def __init__(self, pattern_id, string, db, response):
        self.id = pattern_id
        self.string = string
        self.db = db
        self.response = response


class Query(object):
    def __init__(self, database, query, tokens):
        self.database = database
        self.query = query
        self.tokens = tokens


class PreSQLiClassifier(object):
    # FIXME: Error handling for errors in the xml file
    def __init__(self):
        # TODO: check if file exists
        #directory of sql.py
        file_dir = os.path.dirname(os.path.abspath(__file__))
        patterns_file = os.path.join(file_dir, 'sql_utils', 'patterns.xml')
        self.tree = parse(patterns_file)

    def _get_patterns(self):
        patterns = self.tree.getElementsByTagName("pattern")
        return patterns

    def _getText(self, nodelist):
        rc = []
        for node in nodelist:
            if (node.nodeType == node.TEXT_NODE or
                        node.nodeType == node.CDATA_SECTION_NODE):
                rc.append(node.data)
                break
        return ''.join(rc)

    def _parse_pattern(self, pattern):
        pattern_id = self._getText(
            pattern.getElementsByTagName("id")[0].childNodes)
        pattern_string = self._getText(
            pattern.getElementsByTagName("string")[0].childNodes)
        db = self._getText(pattern.getElementsByTagName("db")[0].childNodes)
        response = self._getText(
            pattern.getElementsByTagName("response")[0].childNodes)
        parsed_pattern = Pattern(
            pattern_id, pattern_string, db, response)
        return parsed_pattern

    def _chr_rep(self, match):
        return chr(int(match.group(1)))

    def _char2string(self, parameter):
        return re.sub('CHAR\(([0-9]*)\)', self._chr_rep, parameter)

    def _deobfuscate(self, parameter):
        parameter = urllib.unquote(parameter)
        parameter = self._char2string(parameter)
        return parameter

    def classify_request(self, parameter):
        patterns = self._get_patterns()
        matched_patterns = []
        for pattern in patterns:
            parsed_pattern = self._parse_pattern(pattern)
            re_pattern = re.compile(parsed_pattern.string, re.IGNORECASE)
            # TODO: Rules for specific method. We should add a tag in the rule
            # to identify which rule it applies.
            # And some forms would send data in GET and POST methods.
            if parameter != '':
                url_match = re_pattern.match(parameter)
                if url_match != None:
                    matched_patterns.append(parsed_pattern)
        return matched_patterns


class QueryCleaner(object):
    def __init__(self):
        pass

    def _ascii_rep(self, match):
        matched_string = match.group()
        return binascii.unhexlify(matched_string[2:])

    def _hex_replace(self, parameter):
        return re.sub('0x[0-9a-fA-F]*', self._ascii_rep, parameter)

    def _parenthetic_contents(self, string):
        stack = []
        for i, c in enumerate(string):
            if c == '(':
                stack.append(i)
            elif c == ')' and stack:
                start = stack.pop()
                if len(stack) == 0:
                    return (len(stack), string[start + 1: i])
                else:
                    continue

    def _process_concat_params(self, param_list):
        processed_params = []
        for param in param_list.split(','):
            if param.startswith('0x'):
                processed_params.append(self._hex_replace(param))
            elif "CASE" in param:
                processed_params.append('1')
            elif "RAND(0)" in param:
                processed_params.append('0')
        return processed_params

    def _find_concat(self, query):
        part = query.split('CONCAT', 1)[1].split(' FROM', 1)[0]
        return 'CONCAT' + part.strip()

    def solve_concat(self, query):
        concat = self._find_concat(query)
        clean_params = self._process_concat_params(
            self._parenthetic_contents(concat)[1])
        solved_query = query.replace(concat, ''.join(clean_params))
        return solved_query


class SQLParser(object):
    def __init__(self):
        self.parser = None

    def _lexical_analysis(self, query):
        self.tokens = []
        query_stream = antlr3.ANTLRStringStream(query)
        lexer = SQLiteLexer(query_stream)
        for token in lexer:
            self.tokens.append(token.getType())
        lexer.reset()
        return antlr3.CommonTokenStream(lexer)

    def _parse_tokens(self, token_stream, parser_rule):
        ret = None
        self.parser = SQLiteParser(token_stream)
        try:
            ret = getattr(self.parser, parser_rule)()
        except Exception as e:
            print "SQLParser error:", e
        return ret

    def _classify(self, query, parser_rule):
        token_stream = self._lexical_analysis(query)
        result = self._parse_tokens(token_stream, parser_rule)
        if result is not None:
            if result.tree is not None:
                self.tree = result.tree.toStringTree()
        return result

    def parser_query(self, query, rule="sql_stmt_list"):
        query = urllib.unquote(query)
        while len(query) > 0:
            res = self._classify(query, rule)
            if res == None:
                break
            syntax_errors = self.parser.getNumberOfSyntaxErrors()
            if syntax_errors == 0:
                break
            if res.getStart().stop == None:
                break
            else:
                if "mismatched input '<EOF>' expecting RPAREN" in self.parser.error:
                    query += ')'
                if "SLEEP" in query.upper():
                    query = 'SELECT ' + query[res.getStart().stop + 3:]
                else:
                    query = query[res.getStart().stop + 1:]


class QueryComparer(object):
    def __init__(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        queries_file = os.path.join(file_dir, 'sql_utils', 'queries.xml')
        tree = ElementTree.parse(queries_file)
        doc = tree.getroot()
        self.queries = doc.findall("query")

    def _token_squence_matcher(self, query_tokens):
        best_ratio = 0.0
        best_query = None
        for query in self.queries:
            tokens = [int(i) for i in query.find("tokens").text.strip().split(', ')]
            ratio = difflib.SequenceMatcher(None, query_tokens, tokens).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_query = query
            if best_ratio == 1.0:
                break
        return best_query, best_ratio

    def _query_string_match(self, payload):
        ratio = 0.8
        queries = [query.find("query").text.strip() for query in self.queries]
        best_matches = difflib.get_close_matches(payload, queries, 1, ratio)
        if len(best_matches) > 0:
            for query in self.queries:
                if query.find("query").text.strip() == best_matches[0]:
                    return query, ratio
        return None, None

    def query_similarity(self, query_tokens, payload):
        best_query, best_ratio = self._query_string_match(payload)
        if best_query is None:
            best_query, best_ratio = self._token_squence_matcher(query_tokens)
        return best_query, best_ratio


if __name__ == "__main__":
    s = ")%20aND%20SLeeP(1)%20And%20(4673%3D4673"
    s = urllib.unquote(s)
    #pre = PreSQLiClassifier('sql_utils/patterns.xml')
    #print pre.classify_request('(())')
    c = SQLParser()
    c.parser_query(s)
    print c.tokens
    print c.tree
