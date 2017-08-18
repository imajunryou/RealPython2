import sqlite3

from random import randint

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("""DROP TABLE IF EXISTS orders""")
    c.execute("""CREATE TABLE IF NOT EXISTS orders
                        (make TEXT, model TEXT, order_date TEXT)
                     """)
    c.execute("SELECT make, model FROM inventory")

    rows = c.fetchall()

    orders = []
    for make, model in rows:
        for _ in range(randint(3, 10)):
            year = randint(2015, 2020)
            month = randint(1, 12)
            day = randint(1, 28)
            date = "{:4}-{:02}-{:02}".format(year, month, day)
            orders.append((make, model, date))

    print("Created", len(orders), "orders...")
    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)

    c.execute("""SELECT orders.make, orders.model, order_date, quantity
                 FROM inventory, orders
                 WHERE orders.make = inventory.make
                 AND orders.model = inventory.model
                 ORDER BY orders.make, orders.model, order_date
                 """)

    rows = c.fetchall()

    print("Orders for each car model:")

    prev_make = None
    prev_model = None
    nl = ""
    for make, model, order_date, quantity in rows:
        if prev_make is not None:
            nl = "\n"
        if not make == prev_make:
            prev_make = make
        if not model == prev_model:
            prev_model = model
            print("{}{} {}:".format(nl, make, model))
            print("{} in stock".format(quantity))
        print("    {}".format(order_date))
