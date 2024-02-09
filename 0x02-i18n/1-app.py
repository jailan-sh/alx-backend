#!/usr/bin/env python3
"""Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


@app.route('/')
def homePage():
    """home page"""
    return render_template('0-index.html')


if __name__ == ('__main__'):
    app.run()
