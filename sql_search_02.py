# Select statement using fetchall to remove unicode characters (no brackets and stuff too)

#Import sqlite3
import sqlite3

#connect to database and make a cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#select the first name and last name from the employees table in database
	c.execute("SELECT firstname, lastname from employees")

	#fetchall() retrieves all records from the query and stores as a list of tuples and assigns to rows variable
	rows = c.fetchall()

	#output the rows on the screen, row by row by using index notation to select items in tuples
	for r in rows:
		print(r[0], r[1])