import sqlite3
import datetime
import threading


class DorkDB(object):
    sqlite_lock = threading.Lock()

    def __init__(self):
        self.conn = sqlite3.connect("db/dork.db")

    def create(self):
        with DorkDB.sqlite_lock:
            self.cursor = self.conn.cursor()
            tablename = ["intitle", "intext", "inurl", "filetype", "ext", "allinurl"]
            for table in tablename:
                sql = "CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY, content TEXT, count INTEGER, firsttime TEXT, lasttime TEXT)" % table
                self.cursor.execute(sql)
            self.cursor.close()
            self.conn.commit()

    def insert(self, insert_list):
        if len(insert_list) == 0:
            return
        try:
            with DorkDB.sqlite_lock:
                for item in insert_list:
                    self.cursor = self.conn.cursor()
                    sql = "SELECT * FROM %s WHERE content = ?" % item['table']
                    cnt = self.cursor.execute(sql, (item['content'],)).fetchall()
                if len(cnt) == 0:
                    self.trueInsert(item['table'], item['content'])
                else:
                    self.update_entry(item['table'], cnt)
                    self.conn.commit()
        except sqlite3.ProgrammingError, e:
            print "In finding error:", e

    def trueInsert(self, table, content):
        try:
            self.cursor = self.conn.cursor()
            sql = "INSERT INTO %s VALUES( ?, ?, ?, ?, ?)" % table
            self.cursor.execute(sql, (None, content, 1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            self.cursor.close()
        except sqlite3.OperationalError, e:
            print "Insert into database Error:", e
        except sqlite3.ProgrammingError, e:
            print "programming error", e

    def update_entry(self, table, cnt):
        self.cursor = self.conn.cursor()
        try:
            sql = "UPDATE %s SET lasttime = ? , count = count + 1 WHERE content = ?" % table
            self.cursor.execute(sql, (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cnt[0][1]))
            self.cursor.close()
            self.conn.commit()
        except sqlite3.OperationalError, e:
            print "Update column failure:", e

    def get_dork_list(self, table):
        with DorkDB.sqlite_lock:
            self.cursor = self.conn.cursor()
            sql = "SELECT content FROM %s" % table
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        return res
