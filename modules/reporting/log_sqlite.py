import sqlite3

class LogSQLite(object):
    
    def __init__(self):
        connection = sqlite3.connect("event_sqlite.db")
        self.cursor = connection.cursor()
    def create(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXIST glastopf.events(id INTEGER PRIMARY KEY, timestamp TEXT, source_ip TEXT, request TEXT, module INTEGER)""")
    def insert(self, data):
        self.cursor.execute("""INSERT INTO glastopf.events VALUES (?,?,?,?,?)""", data)