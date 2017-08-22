# blog.py - controller

# imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
from functools import wraps

# configuration
DATABASE = "blog.db"
USERNAME = "admin"
PASSWORD = "admin"
# Generated with os.urandom(24) after importing os in an interpreter session
SECRET_KEY = "\x81\xb4r\x0e\xeb\xfe\x9251\x90\xa8\x96\xb8\xd2\xd6\x13\xeb\x90\xb5\x81k\xedn\xcc"


app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables in this file
app.config.from_object(__name__)
# Pulls in config from environment variable
# use the following line to establish the default path for it:
# export FLASK_BLOG_SETTINGS=settings.cfg
app.config.from_envvar("FLASK_BLOG_SETTINGS")

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config["DATABASE"])

# used as a decorator to require routes to have valid login credentials
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return test(*args, **kwargs)
        else:
            flash("You need to log in first.")
            return redirect(url_for("login"))
    return wrap

# views

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    status_code = 200
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"] or \
            request.form["password"] != app.config["PASSWORD"]:
            error = "Invalid credentials.  Please try again."
            status_code = 401
        else:
            session["logged_in"] = True
            return redirect(url_for("main"))
    return render_template("login.html", error=error), status_code

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("login"))

@app.route("/add", methods=["POST"])
@login_required
def add():
    title = request.form["title"]
    post = request.form["post"]
    if not title or not post:
        flash("All fields are required.  Please try again.")
        return redirect(url_for("main"))
    else:
        g.db = connect_db()
        g.db.execute("INSERT INTO posts (title, post) VALUES (?, ?)",
                     [request.form["title"], request.form["post"]])
        g.db.commit()
        g.db.close()
        flash("New entry was successfully posted!")
        return redirect(url_for("main"))

@app.route("/main")
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM posts")
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template("main.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
