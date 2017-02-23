# Import SQLite3
import sqlite3

#create a database connection called "cars"
conn = sqlite3.connect("cars.db")

#Create the cursor to execute commands
cursor = conn.cursor()

#create a table/query called inventory that includes "make, model and quantity"
#use the cursor to execute this!
cursor.execute("""CREATE TABLE inventory
               (Make TEXT, Model TEXT, Quantity INT)
               """)

#close the connection
conn.close()
