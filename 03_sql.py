# Using "executemany()" to run a number of sql statements at once

#import sqlite3
import sqlite3

#use a with statement to connect to the database
with sqlite3.connect("new.db") as connection:
    #create a cursor
    c = connection.cursor()

    #insert multiple records from a tuple
    cities = [
        ('Boston', 'MA', 600000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000),
    ]

    #insert the data into the table using executemany
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

#notes for me: the ??? in this statement above is "Paramaterised"
#This protects against SQL injections, always use!
