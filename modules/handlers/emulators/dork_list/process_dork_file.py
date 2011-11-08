import codecs
import re
import gen_dork_db
import unicodedata

class DorkFileProcessor(object):
    
    def __init__(self):
        pass
    
    def get_lines(self):
        dork_lines = []
        with codecs.open("dorks.txt", "r", "utf-8") as dork_list:
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
        dork_db = gen_dork_db.LogDork()
        dork_db.create()
        for dork_line in dork_lines:
            if "intitle:" in dork_line:
                dork_line_split = dork_line.partition('intitle:')[2]
                dork_db.insert("intitle", self.extract_term(dork_line_split))
            if "inurl:" in dork_line:
                dork_line_split = dork_line.partition('inurl:')[2]
                dork_db.insert("inurl", self.extract_term(dork_line_split))
            if "intext:" in dork_line:
                dork_line_split = dork_line.partition('intext:')[2]
                dork_db.insert("intext", self.extract_term(dork_line_split))
            if "filetype:" in dork_line:
                dork_line_split = dork_line.partition('filetype:')[2]
                dork_db.insert("filetype", self.extract_term(dork_line_split))
            #ext is an filetype alias
            if "ext:" in dork_line:
                dork_line_split = dork_line.partition('ext:')[2]
                dork_db.insert("ext", self.extract_term(dork_line_split))
            if "allinurl:" in dork_line:
                dork_line_split = dork_line.partition('allinurl:')[2]
                dork_db.insert("allinurl", self.extract_term(dork_line_split))
        dork_db.closeHandle()
    
    def process_dorks(self):
        dork_lines = self.get_lines()
        self.parse_lines(dork_lines)
