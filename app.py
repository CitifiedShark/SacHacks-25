import pandas as pd
import numpy as n
import sqlite3
# from datetime import datetime

from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import SubmitField
from start1 import make_ai_call

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sadlfsdbkg'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'


## Initialize the database we'll use to store the name:quant:exp of food
def initialize_database():
    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.execute('''CREATE TABLE IF NON EXISTS 
        food (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, expiration DATE)''')
    connector.commit()
    connector.close()

initialize_database()


## Route to the homepage
@app.route("/")
def home():
    return render_template(' ')


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validator=[
            FileAllowed(photos, 'You must upload an image'),
            FileRequired('Please upload a file')
        ]
    )
    submit = SubmitField('Upload')

@app.route("/uploads/<filename>")
def getfilename(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.route("/upload_items", methods=['POST', 'GET'])

def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        image_components = make_ai_call(file_url).split(':')
        connector = sqlite3.connect('thefridge.db') 
        c = connector.cursor()
        ## Convert List into record for Sql data base ??? 
        c.execute("")
    else:
        file_url = None
    
    ## Doesnt do anythin
    return


# @app.route("/add_items", methods=['POST'])
def item_add():
    data = request.json
    name= data['name']
    quantity = int(data['quantity'])
    expiration = data['expiration']

    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.execute("INSERT INTO food (namne, quantity, expiration) VALUES (?, ?, ?)", (name, quantity, expiration))
    connector.commit()
    connector.close()

# @app.route('/get_items', methods=['GET'])
def get_items():
    connector = sqlite3.connect("thefridge.db")
    c = connector.cursor()
    c.execute("SELECT * from items")
    items = c.fetchall()
    connector.close()

    return jsonify({"items": items})



if __name__ == '__main__':
    app.run(debug=True)
