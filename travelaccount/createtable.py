import sqlite3

conn=sqlite3.connect("travel.db")
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS item") 
cur.execute("DROP TABLE IF EXISTS receipt") 
cur.execute("DROP TABLE IF EXISTS travel")

cur.execute("""CREATE TABLE IF NOT EXISTS travel
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT NOT NULL); """)


cur.execute("""CREATE TABLE IF NOT EXISTS receipt
            ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
            travel_id INTEGER NOT NULL,
            date DATE NOT NULL, 
            rate REAL NOT NULL,
            currency TEXT NOT NULL, 
            company TEXT NOT NULL,
            payment TEXT NOT NULL,
            FOREIGN KEY (travel_id) REFERENCES travel(id) ); """)

cur.execute(""" CREATE TABLE IF NOT EXISTS item 
            ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
            receipt_id INTEGER NOT NULL, 
            name TEXT NOT NULL, 
            quantity REAL DEFAULT 1, 
            cost REAL NOT NULL, 
            FOREIGN KEY (receipt_id) REFERENCES receipt(id) ); """)

conn.commit()
conn.close()

