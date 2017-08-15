import csv
import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS employees(firstname TEXT, lastname TEXT)")

    with open("employees.csv", "rU") as emp_csv:
        employees = csv.reader(emp_csv)
        c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)
