from flask import Flask, render_template, request, redirect, url_for, session
import logging
import os
import pdfplumber
import re
from encryption_utils import encrypt_text, decrypt_text
from Crypto.Random import get_random_bytes
from PIL import Image
import pytesseract

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key'

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='my_app.log'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Process the file based on its type
        if file.filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            text = extract_text_from_image(file_path)
        else:
            with open(file_path, 'r') as f:
                text = f.read()

        # Encrypt the text
        secret_key = get_random_bytes(16)  # Generate a random key for encryption
        encrypted_data = encrypt_text(secret_key, text)
        
        # Debugging the encrypted data
        print(f'Encrypted: {encrypted_data.hex()}')

        # Decrypt the text for demonstration purposes (remove in production)
        decrypted_text = decrypt_text(secret_key, encrypted_data)
        print(f'Decrypted: {decrypted_text}')

        # Find emails in the text
        email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        found_emails = email_pattern.findall(decrypted_text)

        return render_template('results.html', emails=found_emails)
    return 'File upload failed!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Simple authentication
            session['username'] = username
            logging.info(f"User {username} logged in")
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    logging.info(f"User {session.get('username')} logged out")
    session.pop('username', None)
    return redirect(url_for('index'))

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

def extract_text_from_image(image_path):
    text = ""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
