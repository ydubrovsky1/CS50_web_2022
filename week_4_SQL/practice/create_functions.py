#create a function to query DB and return all records

def show_all():
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM flights")   
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

    #called in use function

#add a new record to the table
def add_one(id, origin, destination, duration):
    import sqlite3
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("INSERT INTO flights VALUES (?,?, ?, ?)", id, origin, destination, duration)


    #will push changes into the database
    conn.commit()

    #close our connection
    conn.close()