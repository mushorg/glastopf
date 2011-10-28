import gen_html
import process_dork_file
from random import choice, shuffle
import hashlib
import codecs

def prepare_text():
    line_list = []
    with codecs.open("pride.txt", "r", "utf-8") as text_file:
        for text_line in text_file.readlines():
            text_line = text_line.strip()
            if text_line != "":
                line_list.append(text_line.encode('utf-8'))
    number_lines = len(line_list)
    return line_list

def generate_dork_pages():
    line_list = prepare_text()
    processor = process_dork_file.DorkFileProcessor()
    dork_dict = processor.process_dorks()
    shuffle(line_list)
    shuffle(dork_dict['inurl'])
    shuffle(dork_dict["intext"])
    while len(dork_dict['inurl']) > 50:
        body = ''
        for i in range(0,49):
            body += line_list[i] + " <a href='%s'>%s</a> " % (dork_dict['inurl'].pop(), choice(dork_dict["intext"]))
        dork_page = gen_html.html_template(choice(dork_dict['intitle']), "http://www.google.com", body, "Epic Footer Powered By", gen_html.css())
        page_md5 = hashlib.md5(dork_page).hexdigest() 
        with codecs.open("pages/%s" % page_md5, "w", "utf-8") as dork_file:
            dork_file.write(dork_page)
generate_dork_pages()