#output the car info on seperate lines.

#import sqlite3
import sqlite3

#connect to the database and make a cursor
with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	#select the cars make and model and quanity
	c.execute("SELECT make, model, order_date FROM orders")

	#assign selected data to a variable
	rows = c.fetchall()

	#print the data on seperate lines
	for row in rows:
		print("Make: " + row[0])
		print("Model: " + row[1])
		print("Order Date: " + row[2])
		print("")