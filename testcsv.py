#Import csv and sqlite3
import sqlite3
import csv

#create a database/connect if exists
with sqlite3.connect("mockdata.db") as connection:
    #create a cursor
    c = connection.cursor()

    #open the csv file
    people = csv.reader(open("MOCK_DATA.csv", "rU"))

    #create a new table in the database
    c.execute("CREATE TABLE people (firstname TEXT, lastname TEXT, email TEXT, gender TEXT, currency TEXT)")

    #insert the data into the table
    c.executemany("INSERT INTO people(firstname, lastname, email, gender, currency)\
                  values(?,?,?,?,?)", people)
    
