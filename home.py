import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response
import GrammarChecker as g
import time

app = Flask(__name__)

username = ""
password = ""
text = ""

@app.route('/')
def main():
    return render_template("login.html")

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

    data = {'text': text}
    params = {
        'mkt':'en-us',
        'mode':'proof'
        }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Ocp-Apim-Subscription-Key': api_key,
        }

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
