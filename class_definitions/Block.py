from copy import deepcopy
from hashlib import sha256

class Block(object):
    def __init__(self, index, timestamp, transactions, prev_hash, proof=None):
        self.index = index
        self.timestamp = timestamp
        self.transactions = deepcopy(transactions)
        self.prev_hash = prev_hash
        self.proof = proof
        return

    def get_hash(self):
        
        