import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/home')
def home():
    return 'Hello Home!'

# @app.route('profile/<username>')
# def profile(username):
#     return '<h1>Hello %s</h1>' % username

# @app.route('post/<int: id>')
# def post(id):
#     return '<h1>Hello %s</h1>' % id
