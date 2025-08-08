import os
from flask import Flask, request, render_template, jsonify, redirect, url_for, flash
import time
import random


UPLOAD_FOLDER = 'uploads'
MESSAGE = 'messages'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flashing messages
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        if 'pdf_files' not in request.files:
            flash('No files part')
            return redirect(request.url)

        files = request.files.getlist('pdf_files')

        if not files or all(file.filename == '' for file in files):
            flash('No files selected')
            return redirect(request.url)

        for file in files:
            if file and allowed_file(file.filename):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                flash(f'Uploaded: {file.filename}')
            else:
                flash(f'Skipped (invalid type): {file.filename}')

        return redirect(url_for('upload_files'))

    return render_template('index.html')

@app.route("/calculate")
def calculate():
    # data = request.json
    # prompt = data.get("prompt")

    try:
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",  # Or "gpt-3.5-turbo"
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # reply = response.choices[0].message["content"].strip()
        # time.sleep(2 * 60)  # 2 minutes = 120 seconds
        time.sleep(2 * 3)  # 2 minutes = 120 seconds

        analysis = ["""
        Alternative credit scoring models include alternative credit data, such as rent payments or transactional activity, in addition to or as a replacement for traditional credit scores. This additional data creates a powerful borrower profile. A study by FICO found credit scoring models that incorporate alternative data alongside traditional credit data are more powerful than traditional data alone. 

        Depending on the lender, alternative credit scoring models might include: 
        
        Transactional data, including credit and debit transactions
        
        Rent and utility payments
        
        Social network data 
        
        Website behavioral data, such as how they move through the lender's website.  
        
        Text or voice data during customer service calls 
        
        Survey or interview data 
        
        Lenders can analyze this combined data to create alternative credit scoring models and determine creditworthiness in a different way. However, there are privacy issues with some types of alternative credit data. For example, using social media data presents regulatory challenges and can be influenced by the borrower.
        """]

        score = [
            "will display some scores temp 100"]

        return jsonify({"analysis_report":random.choice(analysis), "score":random.choice(score)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)