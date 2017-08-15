from functools import reduce
import sqlite3

def insertion(cursor, table, data):
    """Insert data into table with given cursor"""
    if cursor is None:
        raise ValueError("Cursor is None!")

    if len(data) == 0:
        raise ValueError("Data is empty!")

    expected_length = len(data[0])
    if not all(map(lambda x: len(x)==expected_length, data)):
            raise ValueError("Data rows have inconsistent length!")

    value_str = "(?"
    for _ in range(expected_length-1):
        value_str += ", ?"
    value_str += ")"

    query_str = "INSERT INTO {} values{}".format(table, value_str)
    try:
        cursor.executemany(query_str, data)
    except sqlite3.OperationalError as err:
        print("Failed to insert data into", table)
        print("Error message:")
        print(err)

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS inventory
                    (make TEXT, model TEXT, quantity INT)
                    """)

    data = [
                ("Ford", "Ichi", 5),
                ("Ford", "Ni", 250),
                ("Ford", "San", 625000),
                ("Honda", "Uno", 6),
                ("Honda", "Dos", 360)
                ]

    insertion(c, "inventory", data)

    try:
        c.execute("""UPDATE inventory SET quantity = 50
                        WHERE make = 'Ford' AND model = 'Ichi'""")
    except sqlite3.OperationalError as err:
        print("Failed to update Ford Ichi quantity")
        print("Error message:")
        print(err)

    c.execute("SELECT * FROM inventory WHERE make = 'Ford'")
    rows = c.fetchall()
    for make, model, quantity in rows:
        print("{} {}: {} in stock".format(make, model, quantity))
