from flask import Flask, render_template
import os
import yaml

app = Flask(__name__)

@app.route("/")
def hello_world():
    flashcards = list()
    dir_name = '../flashcards/'
    for file in os.listdir(dir_name):
        with open(dir_name+file, 'r') as card:
            card = yaml.safe_load(card)
            flashcards.append(card)
    return render_template("index.html", flashcards=flashcards)
