import json
from flask import Flask, jsonify, request
from models.expense import Expense, ExpenseSchema
from models.income import Income, IncomeSchema
from models.transaction_type import TransactionType


"""
To run the server:
    - flask run
"""

transactions = [
    Income("Salary", 1000),
    Income("Dividens", 3000),
    Expense("Pizza", 23),
    Expense("Rock Concert", 150)
]


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/incomes")
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type_ == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)
    
@app.route("/incomes", methods=["POST"])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return "", 204


@app.route("/expenses")
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type_ == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)

