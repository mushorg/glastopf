from random import choice, shuffle
import hashlib
import codecs
import unicodedata

import gen_html
import process_dork_file
import read_dork_db

def prepare_text():
    line_list = []
    with codecs.open("pride.txt", "r", "utf-8") as text_file:
        for text_line in text_file.readlines():
            text_line = text_line.strip()
            if text_line != "":
                line_list.append(unicodedata.normalize('NFKD', text_line).encode('ascii', 'ignore'))
    return line_list

def generate_dork_pages():
    
    line_list = prepare_text()
    processor = process_dork_file.DorkFileProcessor()
    processor.process_dorks()
    shuffle(line_list)
    dork_reader = read_dork_db.ReadDork()
    inurl_list = dork_reader.get_dork_list('inurl')
    intext_list = dork_reader.get_dork_list('intext')
    intitle_list = dork_reader.get_dork_list('intitle')
    shuffle(inurl_list)
    while len(inurl_list) > 50:
        body = ''
        for i in range(0,49):
            body += line_list[i] + " <a href='%s'>%s</a> " % (inurl_list.pop()[0], choice(intext_list)[0])
        dork_page = gen_html.html_template(choice(intitle_list)[0], "http://www.google.com", body, "Epic Footer Powered By", gen_html.css())
        page_md5 = hashlib.md5(dork_page).hexdigest() 
        with codecs.open("pages/%s" % page_md5, "w", "utf-8") as dork_file:
            dork_file.write(dork_page)
generate_dork_pages()