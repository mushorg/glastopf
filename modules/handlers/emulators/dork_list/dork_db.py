import sqlite3
import datetime
import threading


class DorkDB(object):

    def __init__(self):
        self.conn = sqlite3.connect("db/dork.db")
        self.sqlite_lock = threading.Lock()

    def create(self):
        with self.sqlite_lock:
            self.cursor = self.conn.cursor()
            tablename = ["intitle", "intext", "inurl", "filetype", "ext", "allinurl"]
            for table in tablename:
                sql = "CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, content TEXT, count INTEGER, firsttime TEXT, lasttime TEXT)" % table
                self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()

    def insert(self, table, content):
        with self.sqlite_lock:
            if (content == '') or (content is None):
                return
            self.cursor = self.conn.cursor()
            try:
                sql = "SELECT * FROM %s WHERE content = ?" % table
                cnt = self.cursor.execute(sql, (content,)).fetchall()
                self.cursor.close()
                if len(cnt) == 0:
                    self.trueInsert(table, content)
                else:
                    self.update_entry(table, cnt)
            except sqlite3.ProgrammingError, e:
                print "In finding error:", e

    def trueInsert(self, table, content):
        with self.sqlite_lock:
            self.cursor = self.conn.cursor()
            try:
                sql = "INSERT INTO %s VALUES( ?, ?, ?, ?, ?)" % table
                self.cursor.execute(sql, (None, content, 1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            except sqlite3.OperationalError, e:
                print "Insert into database Error:", e
            except sqlite3.ProgrammingError, e:
                print "Insert into database Error:", e
            self.cursor.close()

    def update_entry(self, table, cnt):
        with self.sqlite_lock:
            self.cursor = self.conn.cursor()
            try:
                sql = "UPDATE %s SET lasttime = ? , count = count + 1 WHERE content = ?" % table
                self.cursor.execute(sql, (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cnt[0][1]))
            except sqlite3.OperationalError, e:
                print "Update column failure:", e
            self.cursor.close()

    def get_dork_list(self, table):
        with self.sqlite_lock:
            self.cursor = self.conn.cursor()
            sql = "SELECT content FROM %s" % table
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.cursor.close()
            return res

    def closeHandle(self):
        self.conn.commit()
        self.conn.close()
