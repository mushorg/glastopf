import sqlite3
import datetime
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
sys.setdefaultencoding('utf-8')

class LogDork(object):

    def __init__(self):
        self.conn = sqlite3.connect("dork.db")
        #self.conn.text_factory = str

    def create(self):
        tablename = ["intitle", "intext", "inurl", "filetype", "ext", "allinurl"]
        self.cursor = self.conn.cursor()
        for i in tablename:
            cmd = """CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY,
            content TEXT, firsttime TEXT, lasttime TEXT)""".format(i)
            try:
                self.cursor.execute(cmd)
            except sqlite3.OperationalError:
                print cmd + "************ CMD FAILED *********"
        self.conn.commit()
        self.cursor.close()

    def insert(self, table, content):
        self.cursor = self.conn.cursor()
        cmd = "INSERT INTO {0} VALUES(NULL, '{1}', '{2}', '{3}')".format(table, content, str(datetime.datetime.now()), str(datetime.datetime.now()))
        try:
            self.cursor.execute(cmd)
        except sqlite3.OperationalError:
            print cmd + "************ CMD FAILED *********"
        self.cursor.close()

    def updatetime(self, table, content):
        self.cursor = self.conn.cursor()
        cmd = "UPDATE {0} SET 'lasttime' = {1} WHERE 'content' = {2}".format((table, str(datetime.datetime.now()), content))
        try:
            self.cursor.execute(cmd)
        except sqlite3.OperationalError:
            print cmd + "************ CMD FAILED *********"
        self.cursor.close()

    def closeHandle(self):
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.cursor.close()


