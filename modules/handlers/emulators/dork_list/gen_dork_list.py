from random import choice, shuffle
import hashlib
import codecs
import unicodedata

import gen_html
import process_dork_file
import dork_db
import time
import os


def prepare_text():
    line_list = []
    with codecs.open("modules/handlers/emulators/dork_list/pride.txt", "r", "utf-8") as text_file:
        for text_line in text_file.readlines():
            text_line = text_line.strip()
            if text_line != "":
                line_list.append(unicodedata.normalize('NFKD', text_line).encode('ascii', 'ignore'))
    return line_list

def generate_dork_pages(first):
    if True == first:
        processor = process_dork_file.DorkFileProcessor()
        processor.process_dorks()
    line_list = prepare_text()
    shuffle(line_list)
    dork_reader = dork_db.DorkDB()
    inurl_list = dork_reader.get_dork_list('inurl')
    intext_list = dork_reader.get_dork_list('intext')
    intitle_list = dork_reader.get_dork_list('intitle')
    shuffle(inurl_list)
    while len(inurl_list) > 50:
        body = ''
        for i in range(0,49):
            body += line_list[i] + " <a href='%s'>%s</a> " % (inurl_list.pop()[0], choice(intext_list)[0])
        dork_page = gen_html.html_template(choice(intitle_list)[0], "http://www.google.com", body, "Epic Footer Powered By")
        page_md5 = hashlib.md5(dork_page).hexdigest() 
        with codecs.open("modules/handlers/emulators/dork_list/pages/%s" % page_md5, "w", "utf-8") as dork_file:
            dork_file.write(dork_page)

def remove_old_dork_pages(args, pathname, filenames):
    if pathname != args[0]:
        return
    for i in filenames:
        if os.path.isfile(pathname+i):
            os.remove(pathname+i)

def regular_generate_dork(sleep_time):
    dirname = 'modules/handlers/emulators/dork_list/pages/'
    generate_dork_pages(True)
    if sleep_time <= 0:
        return "sleep time too short!"
    while True:
        time.sleep(sleep_time)
        remove_old_dork = os.path.walk(dirname, remove_old_dork_pages, (dirname,))
        generate_dork_pages(False)
        
def collect_dork(parsed_request):
    dork_reader = dork_db.DorkDB()
    try:
        dork = parsed_request.url.split('?')
        dork_reader.insert("inurl", dork)
        dork_reader.closeHandle()
    except:
        print("parsed_request split error for '?'")
        pass

