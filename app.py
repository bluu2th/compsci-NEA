from flask import Flask, jsonify, render_template
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("test.html")