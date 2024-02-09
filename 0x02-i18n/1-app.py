#!/usr/bin/env python3
"""Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """
    configure the avaliable langs in the app
    """
    LANGUAGE = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slash=False)
def homePage() -> str:
    """home page"""
    return render_template('1-index.html')


if __name__ == ('__main__'):
    app.run()
