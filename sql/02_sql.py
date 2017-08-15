# Create a SQLite3 database and table
# Use the INSERT command

# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS population
                        (city TEXT, state TEXT, population INT)
                        """)

cursor.execute("""INSERT INTO population VALUES('New York City',
               'NY', 8400000)
               """)
cursor.execute("""INSERT INTO population VALUES('San Francisco',
                'CA', 800000)""")

# commit the changes
conn.commit()

# close the database connection
conn.close()
