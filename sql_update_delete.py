# Update and Delete statements

#Import sqlite3
import sqlite3

#connect and create a cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#update the data, where the city is New York City, set the population to 9000000
	c.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City'")

	#delete data, from the population table, where the city is boston, delete the data
	c.execute("DELETE FROM population WHERE city = 'Boston'")

	#print new data in caps with new lines above and below
	print("\nNEW DATA:\n")

	#select all from the population table
	c.execute("SELECT * FROM population")

	#assign everything that is selected to the rows variable
	rows = c.fetchall()

	#for each row in the rows variable, print each item
	for r in rows:
		print(r[0], r[1], r[2])

