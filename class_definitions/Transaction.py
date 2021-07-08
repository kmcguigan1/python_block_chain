from random import randint

class Transaction(object):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        return
    
    def dict_repr(self):
        return {'sender':self.sender,'receiver':self.receiver,'amount':self.amount}