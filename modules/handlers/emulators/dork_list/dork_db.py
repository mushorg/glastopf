import sqlite3
import datetime

class DorkDB(object): 

    def __init__(self):
        self.conn = sqlite3.connect("dork.db")

    def create(self):
        self.cursor = self.conn.cursor()
        tablename = ["intitle", "intext", "inurl", "filetype", "ext", "allinurl"]
        for table in tablename:
            sql = "CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, content TEXT, firsttime TEXT, lasttime TEXT)" % table
            self.cursor.execute(sql)
        self.conn.commit()
        self.cursor.close()

    def insert(self, table, content):
        self.cursor = self.conn.cursor()
        try:
            sql = "SELECT * FROM %s WHERE content = ?" % table
            cnt = len(self.cursor.execute(sql, (content,)).fetchall())
            self.cursor.close()
            if cnt == 0:
                print cnt
                self.trueInsert(table, content)
            else:
                print cnt
                self.updatetime(table,content)
        except sqlite3.ProgrammingError, e:
            print "In finding error:", e



    def trueInsert(self, table, content):
        self.cursor = self.conn.cursor()
        print "insert:", content
        try:
            sql = "INSERT INTO %s VALUES( ?, ?, ?, ?)" % table
            self.cursor.execute(sql, (None, content, str(datetime.datetime.now()), str(datetime.datetime.now())))
        except sqlite3.OperationalError, e:
            print "Insert into database Error:", e
        except sqlite3.ProgrammingError, e:
            print "Insert into database Error:", e
        self.cursor.close()

    def updatetime(self, table, content):
        self.cursor = self.conn.cursor()
        try:
            sql = "UPDATE %s SET lasttime = ? WHERE content = ?" % table
            self.cursor.execute(sql, (str(datetime.datetime.now()), content))
        except sqlite3.OperationalError, e:
            print "Update column failure:", e
        self.cursor.close()

    def get_dork_list(self, table):
        self.cursor = self.conn.cursor()
        sql = "SELECT content FROM %s" % table
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.cursor.close()
        return res

    def closeHandle(self):
        self.conn.commit()
        self.conn.close()
