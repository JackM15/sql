# JOINing data from multiple tables - cleaned

#import sqlite3
import sqlite3

#connect to the database and make a cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#select the stuff from multiple tables
	#Select distinct(individual) values from each table where the population and region city match
	#order it ascended using the population.city column, it'll be alphabetical
	c.execute("""SELECT DISTINCT population.city, population.population,
		regions.region FROM population, regions WHERE
		population.city = regions.city
		ORDER by population.city ASC""")

	#fetch all the selected data and place it into a variable
	rows = c.fetchall()

	#print 'em
	for row in rows:
		print("City: " + row[0])
		print("Population: " + str(row[1]))
		print("Region: " + row[2])
		print("")