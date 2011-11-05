import sqlite3
import datetime

class LogDork(object): 

    def __init__(self):
        try:
            self.conn = sqlite3.connect("dork.db")
        except sqlite3.OperationalError: # can't locate database
            print "Please locate dork.db file"
            exit(1)
        self.cursor = self.conn.cursor()

    def create(self):
        tablename = ["intitle", "inttext", "inurl", "filetype", "ext", "allinurl"]
        for i in tablename:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS 
            ?(id INTEGER PRIMARY KEY, content TEXT, firsttime TEXT, lasttime TEXT)""", i)
        self.conn.commit()

    def insert(self, table, content):
        try:
            self.cursor.execute("INSERT INTO ? VALUES( ?, ?, ?, ?)",
            (table, None, content, str(datetime.datetime.now()), str(datetime.datetime.now())))
        except sqlite3.OperationalError:
            print "***** Insert into database Error!! *****"

    def updatetime(self, table, content):
        try:
            self.cursor.execute("UPDATE ? SET 'lasttime' = ? WHERE 'content' = ?", 
            (table, str(datetime.datetime.now()), content))
        except sqlite3.OperationalError:
            print "***** Update column failure!! *****"

    def closeHandle(self):
        self.conn.commit()
        self.cursor.close()


