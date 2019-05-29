import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def idimage():
    form = request.form

    img = form["image"]

    return img

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
