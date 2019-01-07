from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Guess the language</h1>"


if __name__=="__main__":
	app.run(debug=True)
