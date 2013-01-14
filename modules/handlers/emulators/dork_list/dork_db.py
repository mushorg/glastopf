import sqlite3
import datetime
import threading
import logging
from process_dork_file import DorkFileProcessor

logger = logging.getLogger(__name__)


class DorkDB(object):
    """
    Responsible for communication with the sqlite dork database.
    """

    sqlite_lock = threading.Lock()

    def __init__(self, dork_db_path="db/dork.db"):
        self.conn = sqlite3.connect(dork_db_path, check_same_thread = False)
        cursor = self.conn.cursor()
        #Indicates if database has the correct schema
        cursor.execute("SELECT name FROM sqlite_master WHERE name ='intitle'")
        if len(cursor.fetchall()) == 0:
            self.create()
            dorkFileProessor = DorkFileProcessor(self)
            dorkFileProessor.process_dorks()

    def create(self):
        with DorkDB.sqlite_lock:
            self.cursor = self.conn.cursor()
            tablename = ["intitle", "intext", "inurl", "filetype", "ext", "allinurl"]
            for table in tablename:
                sql = "CREATE TABLE IF NOT EXISTS %s (content TEXT PRIMARY KEY, count INTEGER, firsttime TEXT, lasttime TEXT)" % table
                self.cursor.execute(sql)
            self.cursor.close()
            self.conn.commit()

    def insert(self, insert_list):
        if len(insert_list) == 0:
            return
        try:
            with DorkDB.sqlite_lock:
                self.cursor = self.conn.cursor()
                for item in insert_list:
                    sql = "SELECT * FROM %s WHERE content = ?" % item['table']
                    cnt = self.cursor.execute(sql, (item['content'],)).fetchone()
                    if cnt == None:
                        self.trueInsert(item['table'], item['content'])
                    else:
                        self.update_entry(item['table'], cnt, self.cursor)
                self.conn.commit()
        except sqlite3.OperationalError as e:
            logger.exception("Error while inserting into dork_db: {0}".format(e))

    def trueInsert(self, table, content):
        try:
            sql = "INSERT INTO %s VALUES(?, ?, ?, ?)" % table
            self.cursor.execute(sql, (content, 1, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        except sqlite3.OperationalError as e:
            logger.exception("Error while inserting into dork_db: {0}".format(e))

    def update_entry(self, table, cnt, cursor):
        try:
            sql = "UPDATE %s SET lasttime = ? , count = count + 1 WHERE content = ?" % table
            cursor.execute(sql, (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cnt[1]))
        except sqlite3.OperationalError as e:
            logger.exception("Error while updaing column in dork_db: {0}".format(e))

    def get_dork_list(self, table, starts_with=None):
        with DorkDB.sqlite_lock:
            self.cursor = self.conn.cursor()
            if starts_with == None:
                sql = "SELECT content FROM {0}".format(table)
                self.cursor.execute(sql)
            else:
                sql = "SELECT content FROM {0} WHERE content LIKE ?".format(table)
                self.cursor.execute(sql, (starts_with + '%',))
            res = self.cursor.fetchall()

        return_list = []
        for entry in res:
            return_list.append(entry[0])

        return return_list
