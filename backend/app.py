from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/employee")
def employee():
    if request.method == 'POST':
        return register_employee()
    else:
        return get_employees()
    
def register_employee():
    return "ok"

def get_employees():
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)