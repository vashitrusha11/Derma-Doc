from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # for session management
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the UPLOAD_FOLDER exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

users = {
    "username1": "password1",
    "username2": "password2"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            session['logged_in'] = True
            return redirect(url_for('select_option'))
        else:
            return "Invalid credentials! Please try again."
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def select_option():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        option = request.form.get('option')
        return redirect(url_for(option))
    return render_template('select_option.html')

@app.route('/dermadoc')
def dermadoc():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # If the user does not select a file, the browser might submit an empty file part without a filename.
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process the uploaded image
            processed_image_path = process_image(filepath)  # Replace this with your processing logic
            
            return render_template('dermadoc.html', image_path=processed_image_path)

    return render_template('dermadoc.html')

@app.route('/telemedicine')
def telemedicine():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('telemedicine.html')

if __name__ == "__main__":
    app.run(debug=True)
