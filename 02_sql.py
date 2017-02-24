# Using the INSERT command

# Import the SQLite3 library
import sqlite3

# Create the connection object
conn = sqlite3.connect("new.db")

# Make a cursor object to execute SQL commands
cursor = conn.cursor()

# Insert Data
cursor.execute("INSERT INTO population VALUES('New York City', \
               'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
               'CA', 800000)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
