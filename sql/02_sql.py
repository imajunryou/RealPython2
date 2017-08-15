# Create a SQLite3 database and table
# Use the INSERT command
# Roll commit and close into context manager

import sqlite3

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS population
                            (city TEXT, state TEXT, population INT)
                            """)

    cursor.execute("""INSERT INTO population VALUES('New York City',
                   'NY', 8400000)
                   """)

    cursor.execute("""INSERT INTO population VALUES('San Francisco',
                    'CA', 800000)""")
