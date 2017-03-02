#import sqlite 3
import sqlite3

#connect to the database and create a cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#insert multiple records using a tuple
	cities = [
		('Boston', 'MA', 600000),
		('Los Angeles', 'CA', 38000000),
		('Houston', 'TX', 2100000),
		('Philadelphia', 'PA', 1500000),
		('San Antonio', 'TX', 1400000),
		('San Diego', 'CA', 130000),
		('Dallas', 'TX', 1200000),
		('San Jose', 'CA', 900000),
		('Jacksonville', 'FL', 800000),
		('Indianapolis', 'IN', 800000),
		('Austin', 'TX', 800000),
		('Detroit', 'MI', 700000)
	]

	#execute many into the database
	c.executemany("INSERT INTO population VALUES(?,?,?)",cities)

	#select populations where the population value is over 1000000
	c.execute("SELECT * FROM population Where population > 1000000")

	#assign the selected to a variable
	rows = c.fetchall()

	#print the rows of data
	for row in rows:
		print(row[0], row[1], row[2])