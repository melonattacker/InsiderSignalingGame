from flask import Flask, request, jsonify
import json
from sqlclient import *
from equ import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

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
    app.run(debug=True, host='0.0.0.0', port=8080)