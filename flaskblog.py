from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello Bay Ridge World!</p>"

#@app.route("/about")
#def about():
#    return "<h2>This is about your mom</h2>"
## Test Language ##

if __name__ == '__main__':
	app.run(
		debug=True,
		host='0.0.0.0',
		port='5000')
