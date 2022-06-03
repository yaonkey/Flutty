#!/usr/bin/env python3

from flask import Flask, render_template
import os
import toml

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    if (not os.path.exists('flutty.db')):
        pass # todo: install database and create tables
    app.config.from_file("config.toml", load=toml.load)
    app.run(debug=True)