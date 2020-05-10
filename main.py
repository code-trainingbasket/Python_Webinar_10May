import flask

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
	return "<h>My Home Page</h><p>How are you doing today</p>"


if __name__ =='__main__':
	app.run()