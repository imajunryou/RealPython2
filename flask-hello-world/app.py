# ---- Flask Hello World ---- #

from flask import Flask

app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# static route
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!?!?!?!?!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# int converter on dynamic value
@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

# float converter
@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

# path converter, accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

# can define message status explicitly
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello {}".format(name)
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
