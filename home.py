#!pip install opencv-python
#!apt update && apt install -y libsm6 libxext6

import os
from flask import Flask, request, render_template, redirect
from flask import make_response, Response
import base64
import TestCase
# import GrammarChecker as g
import time
import json
import requests
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/app/static/data'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


LD_LIBRARY_PATH='/app'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

text = ""

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/crop', methods=["POST"])
def crop():
    if request.method == 'POST':
      f = request.files['crop_image']

      f.save(secure_filename(f.filename))
        
      return "My Cock"


@app.route('/gay', methods=["POST"])
def getText():
    form = request.form
    image = form["image"]
    
    if request.method == 'POST':
      f = request.files['image']

      f.save(secure_filename(f.filename))
        
      return render_template('crop.html')


    # test.png exists

#     TestCase.first()



@app.route('/gdef', methods=["POST"])
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

    fin_out = d["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    
    return fin_out

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)
