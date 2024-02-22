from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"

@app.route('/welcome')
def welcome():
    return "Welcome to My World"

if __name__ == '__main__':
    app.run(debug=True)