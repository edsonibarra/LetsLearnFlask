import json
from flask import Flask, jsonify


"""
To run the server:
    - flask run
"""

incomes = [
    {"description": "salary", "amount": 5000}
]


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/incomes")
def get_incomes():
    return jsonify(incomes)
