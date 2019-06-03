import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response

app = Flask(__name__)

username = ""
password = ""

@app.route('/')
def main():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
    form = request.form

    username = form["user"]
    password = form["password"]

    return render_template("index.html")


@app.route('/gcheck', methods=["POST"])
def idimage():
    form = request.form
    text = form["text"];
    return img

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
