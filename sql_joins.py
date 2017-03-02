#JOINing data from multiple tables

#import sqlite3
import sqlite3

#connect to the database and create a cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#retrieve the data (tablename.columnname)
	#This one selects the city and population from the population table
	#and the regions from the region table where the population city is equal to the regions city.
	c.execute("""SELECT population.city, population.population,
		regions.region FROM population, 
		regions WHERE population.city = regions.city""")

	#put the selected data into a variable using fetchall
	rows = c.fetchall()

	#print the rows
	for row in rows:
		print(row[0], row[1], row[2])

