from flask import Flask, jsonify, render_template, url_for
import sqlite3
import json

app = Flask(__name__)

# Test route 
# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello(name=None):
#     return render_template("hello.html", person=name)

# Home page
@app.route("/")
def home_page():
    return render_template("home_page.html")


# A page listing all mental health resources from the website (mainly for primary stakeholders)
@app.route("/resources/")
def resources():
    the_resources = [
    {"name": "NHS Mental Health", "url": "https://www.nhs.uk/mental-health/"},
    {"name": "Mind UK", "url": "https://www.mind.org.uk/"},
]
    return render_template("resources.html", resources = the_resources)

# A page listing all mental health resources for people to help out others (secondary stakeholders)
@app.route("/helping_out_others/")
def help_resources():
    help_resources = [
        "hello.com"
    ]
    return render_template("help_resources.html")