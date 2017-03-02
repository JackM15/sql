#create a table and populate it with data
#import sqlite3
import sqlite3

#connect to the database and make a cursor
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#create the table called regions with a city and region column
	c.execute("""CREATE TABLE regions
		(city TEXT, region TEXT)""")

	#add the data to the new table
	cities = [
		('New York City', 'Northeast'),
		('San Francisco', 'West'),
		('Chicago', 'Midwest'),
		('Houston', 'South'),
		('Phoenix', 'West'),
		('Boston', 'Northeast'),
		('Los Angeles', 'West'),
		('Houston', 'South'),
		('Philadelphia', 'Northeast'),
		('San Antonio', 'South'),
		('San Diego', 'West'),
		('Dallas', 'South'),
		('San Jose', 'West'),
		('Jacksonville', 'South'),
		('Indianapolis', 'Midwest'),
		('Austin', 'South'),
		('Detroit', 'Midwest')
	]

	#execute the cursor to add data to the database from the cities tuple
	c.executemany("INSERT INTO regions VALUES(?,?)", cities)

	#select all from regions table and order by region in ascending order.
	c.execute("SELECT * FROM regions ORDER BY region ASC")

	#store the selected values in a vairable
	rows = c.fetchall()

	#print out the row data
	for row in rows:
		print(row[0], row[1])
