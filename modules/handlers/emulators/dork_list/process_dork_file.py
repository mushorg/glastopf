import codecs
import re
import dork_db
import unicodedata


class DorkFileProcessor(object):

    def __init__(self):
        pass

    def get_lines(self):
        dork_lines = []
        with codecs.open("modules/handlers/emulators/dork_list/dorks.txt", "r", "utf-8") as dork_list:
            for dork_line in dork_list.readlines():
                dork_line = dork_line.strip()
                if dork_line != "":
                    dork_lines.append(unicodedata.normalize('NFKD', dork_line).encode('ascii', 'ignore'))
        return dork_lines

    def extract_term(self, dork_line):
        if dork_line.startswith('"'):
            term = re.match('"([^"]+)"', dork_line)
            if term:
                term = term.group(1)
        elif dork_line.startswith("'"):
            term = re.match("'([^']+)'", dork_line)
            if term:
                term = term.group(1)
        else:
            term = dork_line.split(" ")[0]
        if term:
            term = term.strip()
        return term

    def parse_lines(self, dork_lines):
        search_opers = ('intitle:', 'inurl:', 'intext:', 'filetype:', 'ext:', 'allinurl:')
        inserts = []
        for dork_line in dork_lines:
            operator = next((oper for oper in search_opers if oper in dork_line), None)
            if operator != None:
                dork_line_split = dork_line.partition(operator)[2]
                inserts.append({'table': operator[:-1], 'content': self.extract_term(dork_line_split)})

        if len(inserts) > 0:
            dorkdb = dork_db.DorkDB()
            dorkdb.create()
            dorkdb.insert(inserts)

    def process_dorks(self):
        dork_lines = self.get_lines()
        self.parse_lines(dork_lines)
