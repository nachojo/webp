from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<HTML><BODY><H1>print</H1></BODY></HTML>'
if __name__ == '__main__':
	app.run(debug=True)