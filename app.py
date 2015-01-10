#!/bin/env python

from flask import Flask
from questions import questions

app = Flask(__name__)

@app.route("/")
def root():
    print(questions[0]["q"])
    return "Hello World!"

if __name__ == "__main__":
    app.run()
