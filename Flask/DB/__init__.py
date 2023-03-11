DATABASE = "database.db"
import os, sqlite3

def open_db(db = DATABASE):
    with sqlite3.connect(db) as con:
        return con
    
def init_database(DATABASE):
    con = open_db()
    con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    con.close()

if os.path.exists(DATABASE):
    print ("Database exists, moving on...")
else:
    print ("Database does not exist, creating...")
    init_database(DATABASE)