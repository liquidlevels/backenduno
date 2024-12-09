import os
from io import BytesIO
from flask import Flask, flash, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/liquid/py/upload/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return "<p>No file part</p>"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "<p>No selected file</p>"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "<p>success upload</p>"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        
        if 'filename' not in request.form:
            return "<p>No file provided</p>"

        filename = request.form['filename']
        if not filename:
            return "<p>Empty file name provided</p>"
        
        filename = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        if not os.path.exists(file_path):
            return "<p>file does not exist:(</p>"

        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    
    return '''
    <!doctype html>
    <title>Download</title>
    <h1>Download File</h1>
    <form method=post enctype=multipart/form-data>
        <input type=input name=filename>
        <input type=submit value=Download>
    </form>
    '''
