from flask import Flask

app = Flask(__name__)

@app.route('/name')
def get_name():
    return "Boopanapriya"

@app.route('/register_number')
def get_register_number():
    return "22it005"

@app.route('/department')
def get_department():
    return "Information Technology"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


