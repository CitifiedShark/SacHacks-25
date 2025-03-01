import pandas as pd
import numpy as np
import sqlite3
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import SubmitField
from start1 import make_ai_call

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sadlfsdbkg'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

# Initialize the database we'll use to store the user:name:quantity:expiration date of food
def initialize_database():
    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.execute('''CREATE TABLE IF NON EXISTS 
        food (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, expiration DATE)''')
    connector.commit()
    connector.close()

initialize_database()

# Route to the homepage
@app.route("/")
def home():
    return render_template(' ')

## Create a FlaskForm composed for uploading
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

# Route to retrieve uploaded files by filename
@app.route("/uploads/<filename>")
def getfilename(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

# Route to upload images and store extracted information in the database
@app.route("/upload_items", methods=['POST', 'GET'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        image_components = make_ai_call(file_url).split(':')
        connector = sqlite3.connect('thefridge.db') 
        c = connector.cursor()
        # Convert List into record for Sql data base ??? 
        c.execute("")
    else:
        file_url = None
    return

# Route to add food items to the database
# @app.route("/add_items", methods=['POST'])
def item_add():
    data = request.json
    name = data['name']
    quantity = int(data['quantity'])
    expiration = data['expiration']

    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.execute("INSERT INTO food (name, quantity, expiration) VALUES (?, ?, ?)", (name, quantity, expiration))
    connector.commit()
    connector.close()

    return jsonify({"status": "success"})

# Route to retrieve all food items from the database and return them as JSON
# @app.route('/get_items', methods=['GET'])
def get_items():
    connector = sqlite3.connect("thefridge.db")
    c = connector.cursor()
    c.execute("SELECT * FROM food")
    items = c.fetchall()
    connector.close()

    return jsonify({"items": items})

if __name__ == '__main__':
    app.run(debug=True)
