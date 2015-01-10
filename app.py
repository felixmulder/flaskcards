#!/bin/env python
import random
from flask import Flask
from questions import questions
from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
    q_iter = [(k, v) for k, v in questions.items()]

    if len(q_iter) == 0:
        return "YOU ARE WINNER!"

    rand = random.randint(0, len(q_iter)-1)


    question, answer = q_iter[rand]

    del questions[question]

    return render_template("index.html",
                           question=question,
                           left=len(q_iter)-1,
                           answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
