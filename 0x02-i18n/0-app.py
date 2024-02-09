#!/usr/bin/env python3 
"""Basic flask app """
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def homePage():
    return render_template('templates/0-index.html') 
