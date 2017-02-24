# Using the INSERT command

# Import the SQLite3 library
import sqlite3

# Using the "with" keyword, changes are saved automatically without Commit
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', \
              'NY', 8400000)")
    c.execute("INSERT INTO population VALUES('San Francisco', \
              'CA', 800000)")

# Close the connection (DO I NEED TO DO THIS WHEN USING WITH?!?!..)
conn.close()
