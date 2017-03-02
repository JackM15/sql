#Import sqlite3
import sqlite3

#connect and create a cursor
with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	#create a new table called orders
	c.execute("""CREATE TABLE orders
		(make TEXT, model TEXT, order_date TEXT)
		""")

	#add 15 records (3 of each car) with seperate order dates
	c.execute("INSERT INTO orders VALUES('Peugeot', '206', '2016-10-11')")
	c.execute("INSERT INTO orders VALUES('Peugeot', '306', '2016-11-22')")
	c.execute("INSERT INTO orders VALUES('Peugeot', '406', '2016-12-30')")
	c.execute("INSERT INTO orders VALUES('Mercedes', 'E Class', '2002-05-13')")
	c.execute("INSERT INTO orders VALUES('Mercedes', 'C Class', '2013-01-12')")
	c.execute("INSERT INTO orders VALUES('Mercedes', 'S Class', '2011-04-20')")
	c.execute("INSERT INTO orders VALUES('Ferrari', 'California', '2006-10-11')")
	c.execute("INSERT INTO orders VALUES('Ferrari', 'GTC4', '1998-11-12')")
	c.execute("INSERT INTO orders VALUES('Ferrari', 'F12', '2016-12-31')")
	c.execute("INSERT INTO orders VALUES('BMW', 'X5', '2017-10-12')")
	c.execute("INSERT INTO orders VALUES('BMW', '3 Series', '2012-02-25')")
	c.execute("INSERT INTO orders VALUES('BMW', '1 Series', '2013-03-20')")
	c.execute("INSERT INTO orders VALUES('Vauxhall', 'Astra', '2014-07-01')")
	c.execute("INSERT INTO orders VALUES('Vauxhall', 'Corsa', '2006-09-12')")
	c.execute("INSERT INTO orders VALUES('Vauxhall', 'Nova', '1990-02-10')")

	#close the connection
	c.close()