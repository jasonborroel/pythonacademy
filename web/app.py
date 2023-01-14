from flask import Flask, render_template
import os, yaml

app = Flask(__name__)

@app.route("/")
def hello_world():
    flashcards = {}
    with open('../flashcards/quotes.yml') as card:
        card = yaml.load(card)
        flashcards = card
    return render_template("index.html", flashcards=flashcards)
