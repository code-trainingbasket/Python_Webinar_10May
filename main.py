import flask

from flask import render_template

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
	return render_template('home.html',name='Test')

@app.route('/blogs', methods = ['GET'])
def blogs():
	all_blogs = ['Food','Clothes','Computers']
	return render_template('blogs.html',all_blogs = all_blogs)


if __name__ =='__main__':
	app.run()