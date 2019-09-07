from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello, World"
    return render_template('index.html', message=message)