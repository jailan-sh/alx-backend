#!/usr/bin/env python3
"""Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    configure the avaliable langs in the app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def homePage() -> str:
    """home page"""
    return render_template('2-index.html')


if __name__ == ('__main__'):
    app.run()
