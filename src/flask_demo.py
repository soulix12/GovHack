from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route('/dashboard.html')
def dashboard():
    message = "Hello, World2"
    return render_template('dashboard.html', message=message)