# Copyright (C) 2011  Lukas Rist
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sqlite3

class LogSQLite(object):
    # TODO: Add SQLite error handling
    
    def __init__(self):
        self.connection = sqlite3.connect("glastopf.db")
        self.create()
        
    def create(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, timestamp TEXT, source_addr TEXT, request TEXT, module INTEGER, filename TEXT, response TEXT)""")
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