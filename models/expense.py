from models.transaction_type import TransactionType
from models.transaction import Transaction, TransactionSchema
from marshmallow import post_load


class Expense(Transaction):
    def __init__(self, description, amount):
        super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)
        
    def __repr__(self):
        return '<Expense(name={self.description!r})>'.format(self=self)


class ExpenseSchema(TransactionSchema):
    @post_load
    def make_expense(self, data, **kwargs):
        return Expense(**data)
