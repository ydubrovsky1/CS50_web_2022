import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()

#update records
c.execute("""UPDATE flights SET destination = "Cleveland" WHERE origin = "Paris"

""")
c.execute("""UPDATE flights SET destination = "Cleveland" WHERE rowid = 2

""")
#delete records
c.execute("""DELETE from flights WHERE rowid = 2

""")


conn.commit()
conn.close()