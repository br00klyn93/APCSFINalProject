import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response
# import GrammarChecker as g
import time

app = Flask(__name__)

username = ""
password = ""
text = ""

@app.route('/', methods=["POST"])
def main():
    return os.listdir()
#     return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
    form = request.form

    username = form["user"]
    password = form["pass"]

    return render_template("index.html")


@app.route('/gcheck', methods=["POST"])
def gcheck():
    form = request.form
    text = form["text"];

#     if username == "":
#         return render_template('login')

#     g.login("bmclaury93@gmail.com", "brooklyn611")
#     time.sleep(7)

#     g.CheckDocument(text)

    return text

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
