from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello World!</p><h1>Your name is: " + request.args.get('name', 'Jordan') + '</h1>'
