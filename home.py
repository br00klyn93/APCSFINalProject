#!pip install opencv-python
#!apt update && apt install -y libsm6 libxext6

import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response
import TestCase
# import GrammarChecker as g
import time
import json
import requests
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

text = ""

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def getText():
    form = request.form
    # image = form["image"]

    image = request.files.get('image', '')
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Use ethans algo
    return "All Clear"

# @app.route('/gdef', methods=["POST"])
def gcheck():
    form = request.form
    word = form["word"]

    app_id = "60edc74a"
    app_key = "6b8466506d884d62a86f1e2d283f2286"
    language = "en-gb"
    word_id = word
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

    d = json.dumps(r.text)

    fin_out = d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0] + "[" + d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"]

    return fin_out

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
