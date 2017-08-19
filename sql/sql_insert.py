import sqlite3

from random import randint

def rebuild_db():
    with sqlite3.connect("newnum.db") as conn:
        c = conn.cursor()

        nums = [(randint(0, 100),) for _ in range(100)]

        c.execute("""DROP TABLE IF EXISTS numbers""")
        c.execute("""CREATE TABLE IF NOT EXISTS numbers(num INT)""")

        c.executemany("""INSERT INTO nums VALUES(?)""", nums)

if __name__ == "__main__":
    rebuild_db()
