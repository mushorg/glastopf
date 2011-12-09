import sqlite3

conn = sqlite3.connect("db/glastopf.db")
cursor = conn.cursor()

num_of_item = len(cursor.execute("SELECT * FROM events").fetchone())
if num_of_item == 7:
    try:
        cursor.execute("ALTER TABLE events ADD COLUMN ")
    except sqlite3.OperationalError, e:
        print "Add Column Failed ", e
    except sqlite3.ProgrammingError, e:
        print "Add Column Failed " e
    except Exception as e:
        print "Unknow type ", e
    finally:
        conn.commit()

cursor.close()
conn.close()
