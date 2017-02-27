# Importint from CSV

#Import the csv library and sqlite3
import csv
import sqlite3

#connect to the database
with sqlite3.connect("new.db") as connection:
    #create a cursor
    c = connection.cursor()

    #open the csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", "rU"))

    #create a new table called employees in the database file
    c.execute("CREATE TABLE employees(firstname TEXT, lastname Text)")

    #insert the data into the table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?,?)", employees)
