import sqlite3

conn = sqlite3.connect("cars.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS inventory
                (make TEXT, model TEXT, quantity INT)
                """)

conn.close()
