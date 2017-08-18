import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("SELECT count(model) FROM orders GROUP BY model")


