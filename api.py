import os
from flask import Flask, request, jsonify
from clock import setup


app = Flask(__name__)

setup()

@app.route("/", methods=['GET'])
def hello():
    return "Hello, this is the EMF 2016 number '1' sign! To get started, try a GET to <a href='/lights'>/info</a> or <a href='/lights'>/lights</a>."


@app.route('/info', methods=['GET'])
def info():
    return """This API lets you control the lighs in the nember '1' on the hill above the camp.<br/>
    By default it's a binary clock. The top five lights represent the hour and the bottom three lights are the number of 10-minutes into the hour.<br/>
    You can get make the lights flash by GETting <a href='/lights'>/lights</a> (e.g. in your browser)<br/>"""


@app.route('/lights', methods=['GET'])
def demo():
    return "Soon this will run the lights.py functionality.."


@app.route('/lights', methods=['POST'])
def custom():
    return "Soon this will let you post a custom lighting sequence.."


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)