import sql_insert
from easygui import buttonbox, msgbox
import sqlite3

def query_db(op):
    """Query DB using the provided operation"""
    answer = None
    sql = {"AVG": "SELECT AVG(num) FROM nums",
           "MAX": "SELECT MAX(num) FROM nums",
           "MIN": "SELECT MIN(num) FROM nums",
           "SUM": "SELECT SUM(num) FROM nums"
           }

    if op not in sql:
        return answer

    with sqlite3.connect("newnum.db") as conn:
        c = conn.cursor()
        try:
            c.execute(sql[op])
        except sqlite3.OperationalError as err:
            return err
        answer = c.fetchone()

    return answer[0]

if __name__ == "__main__":
    choices = ("AVG", "MAX", "MIN", "SUM", "Reroll", "Exit")
    while True:
        choice = buttonbox("Make a choice", "Select a function", choices)

        if not choice or choice == "Exit":
            msgbox("Goodbye!")
            break
        elif choice == "Reroll":
            sql_insert.rebuild_db()
            msgbox("New numbers have been rolled!")
        elif choice in choices:
            result = query_db(choice)
            msgbox("You selected {} and got the result: {}".format(choice, result))
        else:
            msgbox("You managed to select an odd choice: " + choice)
