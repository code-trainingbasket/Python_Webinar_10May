import flask

from flask import render_template,jsonify,request

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def home():
	return render_template('home.html',name='Test')

@app.route('/blogs', methods = ['GET'])
def blogs():
	all_blogs = ['Food','Clothes','Computers']
	return render_template('blogs.html',all_blogs = all_blogs)


@app.route('/api/v1/resources/checkprime',methods =['GET'])
def check_prime_api():

	if 'num' in request.args:
		n = int(request.args['num'])
	else:
		return "No Number (num) provided "
	prime = False
	for i in range(2,n//2 +1):
		if n% i == 0:
			break
	else:
		prime = True

	result = {'Number':n, "Is Prime":prime}

	return jsonify(result)


if __name__ =='__main__':
	app.run()