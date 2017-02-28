# Import SQLite3
import sqlite3

#create a database connection called "cars"
conn = sqlite3.connect("cars.db")

#Create the cursor to execute commands
cursor = conn.cursor()

#Update the quantity on 2 of the records.
cursor.execute("UPDATE inventory SET quantity = 3 WHERE make = 'Honda' ")

#select all the rows
cursor.execute("SELECT * FROM inventory")

#fetch all the rows to print
rows = cursor.fetchall()

#print all the rows
for row in rows:
	print(row[0], row[1], row[2])

#commit the changes
conn.commit()

#close the connection
conn.close()
