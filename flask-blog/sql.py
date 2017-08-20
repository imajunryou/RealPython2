# sql.py - Create a sqlite3 database and populate it with data

import sqlite3

# create the database if it doesn't already exist
with sqlite3.connect("blog.db") as conn:
    c = conn.cursor()

    # create table to hold post information
    c.execute("""CREATE TABLE IF NOT EXISTS posts
              (title TEXT, post TEXT)
              """)

    # insert dummy data
    data = [
            ("Good", "I'm good."),
            ("Well", "I'm well."),
            ("Excellent", "I'm excellent."),
            ("Okay", "I'm okay.")
            ]
    c.executemany('INSERT INTO posts VALUES(?, ?)', data)
