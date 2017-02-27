# INSERT command with Error Handler

# Import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# Get a cursor object used to exeute sql commands
cursor = conn.cursor()

try:
    #insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
    #commit the changes
    conn.commit()
except sqlite3.OperationalError:
    #print an error messasges
    print("Oops! Something went wrong. Try again...")

#close the database connection
conn.close()
