# Create a SQLite3 database and table
# Use the INSERT command
# Roll commit and close into context manager
# Wrap inserts in a try/except

import sqlite3

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS population
                            (city TEXT, state TEXT, population INT)
                            """)

    try:
        cursor.execute("""INSERT INTO population VALUES('New York City',
                       'NY', 8400000)
                       """)

        cursor.execute("""INSERT INTO population VALUES('San Francisco',
                        'CA', 800000)""")
    except sqlite3.OperationalError as e:
        print("Couldn't insert data into database")
        print("Reported message:")
        print(e)
