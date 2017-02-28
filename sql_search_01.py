# Select Statement

# Import Sqlite3
import sqlite3

# create connection to database and add cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#use a for loop to iterate through the database, printing results line by line
	for row in c.execute("SELECT firstname, lastname from employees"):
		print(row)
