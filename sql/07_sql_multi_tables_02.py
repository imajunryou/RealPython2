import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS regions (city TEXT, region TEXT)")

    cities = [
        ("New York City", "Northeast"),
        ("San Francisco", "West"),
        ("Chicago", "Midwest"),
        ("Houston", "South"),
        ("Phoenix", "West"),
        ("Boston", "Northeast"),
        ("Los Angeles", "West"),
        ("Houston", "South"),
        ("Philadelphia", "Northeast"),
        ("San Antonio", "South"),
        ("San Diego", "West"),
        ("Dallas", "South"),
        ("San Jose", "West"),
        ("Jacksonville", "South"),
        ("Indianapollis", "Midwest"),
        ("Austin", "South"),
        ("Detroit", "Midwest")
    ]

    c.executemany("INSERT INTO regions VALUES(?, ?)", cities)

    c.execute("SELECT * FROM regions ORDER BY region ASC")

    rows = c.fetchall()

    for city, region in rows:
        print(city, region)
