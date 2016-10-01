 # -*- coding: utf-8 -*-
from flask import render_template
from app import app

import re, random
from markov_python.cc_markov import MarkovChain
import os
from settings import APP_STATIC


def badEnd(word):
    wordList = ["our", "the", "if", "for", "i", "we", "or", "and", "to", "a", "he", "she", "our", "they", "of"]
    b = word in (wordList[:])
    return b
def postProcess(ary):
    length = len(ary) - 1
    while(badEnd(ary[length])):
        length -= 1
    postAry = ary[:length + 1]
    postAry = " ".join(postAry)
    return postAry.capitalize() + "."

def read_file(filename, charset='utf-8'):
    with open(filename, 'r') as f:
        return f.read()

def fetch_data(file):
    # quotes = open("app/static/quotes.txt", "r")
    # quotes_str = quotes.readlines().decode('utf-8')
    # quotes.close()
    quotes_str = read_file(file)
    quotes_str = str(quotes_str)
    if file == "app/static/markov.txt":
        answer = "M"
        mc = MarkovChain(3)
        mc.add_string(quotes_str)
        array = mc.generate_text()
        return [postProcess(array), answer]

    else:
        answer = "T"
        sentences = quotes_str.split("\n")
        return [sentences[random.randint(0, len(sentences) - 1)], answer]

@app.route('/')
@app.route('/index')
def index():
    files = ["app/static/markov.txt", "app/static/trump.txt"]
    file = files[random.randint(0,1)]
    sentence = fetch_data(file)
    return render_template("index.html", sentence=sentence[0].upper(), MorT=sentence[1])
