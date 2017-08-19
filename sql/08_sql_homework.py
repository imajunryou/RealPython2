import sqlite3

with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("""SELECT make, model, count(model)
              FROM orders GROUP BY model ORDER BY make DESC
              """)

    rows = c.fetchall()

    print("Total number of orders for each make and model:")
    for make, model, count in rows:
        print("{} {}: {} orders placed".format(make, model, count))

    c.execute("""SELECT orders.make, orders.model,
              inventory.quantity, count(orders.model)
              FROM inventory, orders
              WHERE inventory.make = orders.make AND inventory.model = orders.model
              GROUP BY orders.model
              ORDER BY orders.make DESC
              """)

    rows = c.fetchall()

    print("\n\nOrder information:\n")
    for make, model, quant, orders in rows:
        line = "{} {}\nIn Stock: {}\nOrders placed: {}"
        print(line.format(make, model, quant, orders))
        if quant - orders < 0:
            print("    ** Short by " + str(orders - quant) + " units! **\n")
        else:
            print("\n")
