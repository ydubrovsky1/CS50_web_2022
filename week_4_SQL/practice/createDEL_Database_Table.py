import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor()

#DROP A TABLE
c.execute("DROP TABLE flights1")

#create a table. """ allows use multiple lines
c.execute(""" CREATE TABLE flights1 (
    id integer,
    origin text,
    destination text,
    duration integer
)""")


#create a table. """ allows use multiple lines
c.execute("""CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
)""")

#NULL
#INTEGER
#REAL
#TEXT
#BLOB


c.execute("INSERT INTO flights VALUES ('Paris', 'Columbus', 4)")


#will push changes into the database
conn.commit()

#close our connection
conn.close()