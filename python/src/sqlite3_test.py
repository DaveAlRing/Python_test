import sqlite3

db = sqlite3.connect("books.db")

cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    price real
    );""")

cur.execute("""INSERT INTO books(id, title, author, price)
            VALUES("1", "Untold Stories", "Alan Bennett", "17.49")""")

db.commit()
db.close()