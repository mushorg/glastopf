import sqlite3

class ReadDork(object): 

    def __init__(self):
        pass
        
    def get_dork_list(self, table):
        self.conn = sqlite3.connect("dork.db")
        self.cursor = self.conn.cursor()
        sql = "SELECT content FROM %s" % table
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.conn.close()
        return res