import sqlite3

class LogDork(object): 
    def __init__(self):
		try:
			self.conn = sqlite3.connect("dork.db")
		except sqlite3.OperationalError: # can't locate database
			exit(1)
		self.cursor = self.conn.cursor()

	def create(self):
		
	def insert(self):
		
			

