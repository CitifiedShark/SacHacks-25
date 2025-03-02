import sqlite3
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import SubmitField
from start1 import fetch_analysis 
from index import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'sadlfsdbkg'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[FileAllowed(photos, 'You must upload an image'), FileRequired('Please upload a file')]
    )
    submit = SubmitField('Upload Photo')

# Initialize the database we'll use to store the user:name:quantity:expiration date of food
"""def initialize_database():
    connector = sqlite3.connect('thefridge.db')
    c = connector.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS 
        food (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, expiration DATE)''')
    connector.commit()
    connector.close()
send_from_directory
initialize_database()"""

# Route to the homepage
@app.route("/")
def home():
    return render_template('capture.html')

## Create a FlaskForm composed for uploading


# Route to retrieve uploaded files by filename
@app.route("/uploads/<filename>", methods=['GET'])
def getfilename(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

# Route to upload images and store extracted information in the database
 
@app.route("/upload_items", methods=['POST', 'GET'])
def upload_image():
    valid_file = False
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('getfilename', filename=filename)
        print("DEBUG: ", file_url)
        valid_file = True
        #analysis = fetch_analysis(file_url).split(':')
        #connector = sqlite3.connect('thefridge.db') 
        #c = connector.cursor()

        # Convert List into record for Sql data base ??? 
        #c.execute("INSERT INTO thefridge(name, quantity, expiration) VALUES (?, ?, ?)",analysis[0], analysis[1], analysis[2])
    else:
        file_url = None
    return render_template('uploader.html', form=form, file_url=file_url)

if __name__ == '__main__':
    app.run(debug=True)
