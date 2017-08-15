# Updating and deleting database information

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("""UPDATE population SET population = 9000000
                    WHERE city = 'New York City'""")

    c.execute("""DELETE FROM population WHERE city='Boston'""")

    print("\nNew data:\n")

    c.execute("SELECT * FROM population")
    rows = c.fetchall()

    for city, state, pop in rows:
        print(city, state, pop)
