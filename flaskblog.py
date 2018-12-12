from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '656e74657220796f7572207068726173652068657265'


posts = [
	{
		'author': 'Corey Shafer',
		'title': 'Blog Post 1',
		'content': 'first post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'second post content',
		'date_posted': 'April 21, 2018'
	}

]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')
## Test Language ##

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

	@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
	app.run(
		debug=True,
		host='0.0.0.0',
		port='5000')
