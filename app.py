from flask import Flask, jsonify, render_template
import sqlite3
import json

app = Flask(__name__)

# Testing routing
@app.route("/")
def hello_world():
    return render_template("test.html")


# A page listing all mental health resources from the website
@app.route("/resources/")
def resources():
    the_resources = [
    {"img_url": "cattest.webp", "width": 640, "height": 480},
    {"img_url": "testcat.jpg", "width": 1920, "height": 1080},
]
    return render_template("resources.html", resources = the_resources)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

