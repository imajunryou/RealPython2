# Create a SQLite3 database and table
# Use the INSERT command via executemany method
# Roll commit and close into context manager

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS population
                            (city TEXT, state TEXT, population INT)
                            """)

    # insert multiple records using a tuple
    cities = [
                ('Boston', 'MA', 600000),
                ('Chicago', 'IL', 2700000),
                ('Houston', 'TX', 2100000),
                ('Phoenix', 'AZ', 1500000)
                ]

    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
