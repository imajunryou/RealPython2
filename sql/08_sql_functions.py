import sqlite3


with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    sql = {"average": "SELECT avg(population) FROM population",
           "maximum": "SELECT max(population) FROM population",
           "minimum": "SELECT min(population) FROM population",
           "sum": "SELECT sum(population) FROM population",
           "count": "SELECT count(city) FROM population"
           }

    for key, value in sql.items():
        c.execute(value)

        result = c.fetchone()

        print(key + ":", result[0])
