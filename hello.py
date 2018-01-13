from flask import *



app = Flask(__name__)


@app.route('/hello')
def hello_world():
	user = {'name': 'Peter Delaney'}
	return render_template("hello.html", user=user)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
