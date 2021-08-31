import sqlite3

#connect to database
conn = sqlite3.connect('db.sqlite3')

#create cursor
c = conn.cursor()

#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
c.execute("SELECT rowid, * FROM auctions_user")
num_fields = len(c.description)
field_names = [i[0] for i in c.description]


#print(c.fetchall())

#DROP A TABLE
#c.execute("DROP TABLE auctions_listing")

#c.execute("DELETE from auctions_bid WHERE rowid > 0")

#c.execute("SELECT rowid, * FROM auctions_user")

#items = c.fetchall()

#for item in items:
#    print(item)
#commit our command
#conn.commit()

#close our connection
conn.close()
