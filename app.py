#!/usr/bin/env python

from flask import Flask 

app = Flask(__name__)
guesses = ["Python", "Java", "C++"]


@app.route("/")
def index():
	return "<h1>Guess the language</h1>"


@app.route("/guess/<int:id>")
def guess(id):
	return ("<h1>Guess the language!</h1>"
		     "<p>My guess: {0}</p>").format(guesses[id])

if __name__=="__main__":
	app.run(debug=True)
