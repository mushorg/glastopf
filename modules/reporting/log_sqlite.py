import sqlite3

class LogSQLite(object):
    
    def __init__(self):
        self.connection = sqlite3.connect("glastopf.db")
        self.create()
        
    def create(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, timestamp TEXT, source_ip TEXT, request TEXT, module INTEGER, filename TEXT, response TEXT)""")
        self.connection.commit()
        self.cursor.close()
        
    def insert(self, attack_event):
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                INSERT INTO events VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                (None, attack_event.event_time, attack_event.source_addr[0] + ":" + str(attack_event.source_addr[1]), 
                attack_event.parsed_request.url, attack_event.matched_pattern, 
                attack_event.file_name, attack_event.response))
        self.connection.commit()
        self.cursor.close()