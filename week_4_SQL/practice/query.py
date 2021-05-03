import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()

#query the database
c.execute("SELECT rowid, * FROM flights")

#c.fetchone(), c.fetchmany(3), c.fetchall()

items = c.fetchall()

for item in items:
    print(item)
    #print(item[1] + " "+item[2] )

#print(c.fetchall())
#print(c.fetchone()[0])

#specific queries
samples = c.execute("SELECT rowid, origin, duration FROM flights WHERE duration > 4 ORDER BY origin DESC")
for sample in samples:
    print(sample)
print("\n_________________________\n")

samples = c.execute("SELECT rowid, origin, duration FROM flights WHERE origin LIKE 'P%' OR destination LIKE 'C%' ")
for sample in samples:
    print(sample)
print("\n_______________________\n")

samples = c.execute("SELECT rowid, * FROM flights ORDER BY rowid DESC LIMIT 2")
for sample in samples:
    print(sample)
print("\n_______________________\n")

#commit our command
conn.commit()

#close our connection
conn.close()