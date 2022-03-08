import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
    return home()


@app.route('/home')
def home():
    return 'Hello Home!'
