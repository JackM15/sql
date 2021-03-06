# SQLite Functions

#Import sqlite3
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#create a dictionary of SQL queries
	sql = {'average': 'SELECT avg(population) FROM population',
			'maximum': 'SELECT max(population) FROM population',
			'minimum': 'SELECT min(population) FROM population',
			'sum': 'SELECT sum(population) FROM population',
			'count': 'SELECT count(city) FROM population'}

	#run each sql query in the dictionary by looping over it and executing the values
	for keys,values in sql.items():
		#run sql
		c.execute(values)

		#fetchone() retrieves one record from the query
		result = c.fetchone()

		#output the result to the screen
		print(keys + ":", result[0])