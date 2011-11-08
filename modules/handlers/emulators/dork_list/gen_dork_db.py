import sqlite3
import datetime

class LogDork(object): 

    def __init__(self):
        self.conn = sqlite3.connect("dork.db")
        self.cursor = self.conn.cursor()

    def create(self):
        tablename = ["intitle", "intext", "inurl", "filetype", "ext", "allinurl"]
        for table in tablename:
            sql = "CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, content TEXT, firsttime TEXT, lasttime TEXT)" % table
            self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, table, content):
        print "insert:", content
        try:
            sql = "INSERT INTO %s VALUES( ?, ?, ?, ?)" % table
            self.cursor.execute(sql, (None, content, str(datetime.datetime.now()), str(datetime.datetime.now())))
        except sqlite3.OperationalError, e:
            print "Insert into database Error:", e
        except sqlite3.ProgrammingError, e:
            print "Insert into database Error:", e

    def updatetime(self, table, content):
        try:
            sql = "UPDATE %s SET 'lasttime' = ? WHERE 'content' = ?" % table
            self.cursor.execute(sql, (str(datetime.datetime.now()), content))
        except sqlite3.OperationalError, e:
            print "Update column failure:", e

    def closeHandle(self):
        self.conn.commit()
        self.cursor.close()


