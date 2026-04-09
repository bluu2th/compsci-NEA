from flask import Flask, jsonify, render_template, url_for
import sqlite3
import json

app = Flask(__name__)

# Home page
@app.route("/")
def home_page():
    return render_template("home_page.html")


# A page listing all mental health resources from the website
@app.route("/resources/")
def resources():
    the_resources = [
    
]
    return render_template("resources.html", resources = the_resources)

# Test route 
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", person=name)

# 
@app.route("/helping_out_others/")
def help_resources():
    help_resources = [

    ]
    return render_template("help_resources.html")