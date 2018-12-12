from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Bay Ridge World!</h1>"

#@app.route("/about")
#def about():
#    return "<h2>This is about your mom</h2>"
## Test Language ##

if __name__ == '__main__':
	app.run(host= '0.0.0.0')
