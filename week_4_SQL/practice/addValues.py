import sqlite3

#connect to database
conn = sqlite3.connect('customer.db')

#create cursor
c = conn.cursor()

many_flights = [
    (1, 'Paris', 'Columbus', 4), 
    (2, 'London', 'Columbus',54), 
    (3, 'Prague', 'Columbus', 20)]

c.executemany("INSERT INTO flights VALUES (?,?, ?, ?)", many_flights)

c.execute("INSERT INTO flights VALUES (4,'Tuscany', 'Columbus', 4)")

#will push changes into the database
conn.commit()

#close our connection
conn.close()