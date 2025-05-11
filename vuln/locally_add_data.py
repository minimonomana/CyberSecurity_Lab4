import sqlite3

conn = sqlite3.connect('app/db.sqlite3')
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)")
c.execute("INSERT INTO users (username, email) VALUES ('admin', 'admin@example.com')")
c.execute("INSERT INTO users (username, email) VALUES ('john', 'john@example.com')")
conn.commit()
conn.close()
