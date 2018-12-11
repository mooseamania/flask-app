from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Bay Ridge World!</h1>"

@app.route("/about")
def hello():
    return "<h2>This is about your mom</h2>"
## Test Language ##


