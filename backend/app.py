import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import json
from sqlclient import *
from process import *

ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'
CORS(
    app,
    supports_credentials=True
) #これ

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_and_send_file():
    if request.method == 'POST':
        # post requestにfile partがあるかチェック
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        # ファイル名のチェック
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = process(app.config['UPLOAD_FOLDER'], filename)
            return send_file(
                filepath, as_attachment=True
            )


@app.route("/employee", methods=["GET", "POST"])
def employee():
    if request.method == 'POST':
        return register_employee()
    else:
        return get_employees()
    
def register_employee():
    data = request.json
    print(data["params"]["c_a"])
    best_response = calc_equ(data["params"])
    insert_employee(data["name"], best_response)
    return "ok"

def get_employees():
    employees = query_employees()
    print(employees)
    return json.dumps(employees)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)