# Import SQLite3
import sqlite3

#create a database connection called "cars"
conn = sqlite3.connect("cars.db")

#Create the cursor to execute commands
cursor = conn.cursor()

#insert 5 records of data into the database, 3 fords and 2 hondas.
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 5)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'CR-V', 2)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 4)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Fiesta', 2)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Mondeo', 3)")

#commit the changes
conn.commit()

#close the connection
conn.close()
