from flask import Flask, render_template
import os
import yaml

app = Flask(__name__)

@app.route("/")
def hello_world():
    flashcards = list()
    with open('../flashcards/quoting.yml', 'r') as card:
        card = yaml.safe_load(card)
        flashcards.append(card)
    with open('../flashcards/nesting_functions.yml', 'r') as card:
        card = yaml.safe_load(card)
        flashcards.append(card)        
    return render_template("index.html", flashcards=flashcards)
