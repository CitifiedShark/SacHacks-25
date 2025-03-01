from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as n
import sqlite3
from datetime import datetime
from scan import *

app = Flask(__name__)

def initialize_database():
    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.execute('''CREATE TABLE IF NON EXISTS 
        food (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, expiration DATE)''')
    connector.commit()
    connector.close()

initialize_database()

@app.route("/")
def home():
    return render_template(' ')

@app.route("/add_items", methods=['POST'])


def item_add():
    data = request.json
    name= data['name']
    quantity = int(data['quantity'])
    expiration = data['expiration']

    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.exectue("INSERT INTO food (namne, quantity, expiration) VALUES (?, ?, ?)", (name, quantity, expiration))
    connector.commit()
    connector.close()

@app.route('/get_items', methods=['GET'])
def get_items():
    connector = sqlite3.connect("thefridge.db")
    c = connector.cursor()
    c.execute("SELECT * from items")
    items = c.fetchall()
    connector.close()

    return jsonify({"items": items})



if __name__ == '__main__':
    app.run(debug=True)
