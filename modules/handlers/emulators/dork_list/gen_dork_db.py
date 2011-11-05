import sqlite3

class LogDork(object): 

    def __init__(self):
		try:
			self.conn = sqlite3.connect("dork.db")
		except sqlite3.OperationalError: # can't locate database
			print "Please locate dork.db file"
			exit(1)
		self.cursor = self.conn.cursor()
		self.create()

	def create(self):
		tablename = ["intitle", "inttext", "inurl", "filetype", "ext", "allinurl"]
		cmd = "CREATE TABLE IF NOT EXISTS"
		tableform = "(id INTEGER PRIMARY KEY, content TEXT, firsttime TEXT, lasttime TEXT)"
		for i in tablename:
			self.cursor.execute(cmd+i+tableform)
		self.conn.commit()

	def insert(self):
		cmd = "INSERT INTO"

	def closeHandle(self):
		self.conn.commit()
		self.conn.close()
			

