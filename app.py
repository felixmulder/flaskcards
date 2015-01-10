#!/bin/env python

from flask import Flask
from questions import questions
from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
    print(questions[0]["q"])
    return render_template("index.html",
                           question=questions[0]["q"],
                           answer=questions[0]["a"])

if __name__ == "__main__":
    app.run(debug=True)
