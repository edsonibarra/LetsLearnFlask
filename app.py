import json
from flask import Flask


"""
To run the server:
    - flask run
"""

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
