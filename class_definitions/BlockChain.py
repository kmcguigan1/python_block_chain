import time
from uuid import uuid4
from hashlib import sha256
from copy import deepcopy


class Transaction(object):
    def __init__(self, sender, receiver, amount):
        self.id = uuid4()
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        return
    
    def str_repr(self):
        return f'{self.id}{self.sender}{self.receiver}{self.amount}'

class Block(object):
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index # place in chain, 0 means its the first block
        self.timestamp = timestamp # the time the block was created
        self.transactions = deepcopy(transactions) # the list of transacitons on this block
        self.prev_hash = prev_hash # the hash of the previous block
        self.proof = None # the proof for this block
        return

    def add_proof(self, proof):
        self.proof = proof
        return

    def is_valid(self):
        return self.proof is not None

    def str_repr(self):
        if(not self.is_valid()):
            return None
        str_repr = f"{self.index}{self.timestamp}"
        for transaction in self.transactions:
            str_repr += transaction.str_repr()
        str_repr += f"{self.prev_hash}"
        str_repr += f"{self.proof}"
        return str_repr

    def get_hash(self):
        if(self.is_valid()):
            return sha256(self.str_repr()).hexdigest()
        return None


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.diff_level = 4
        self.create_genesis_block()
        return

    def create_genesis_block(self):
        genesis_block = self.create_block(prev_hash=1)
        return

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        return

    def create_block(self, prev_hash=None):
        if(prev_hash is None):
            prev_hash = self.chain[-1].get_hash()
        new_block = Block(len(self.chain) + 1, time.time(), self.pending_transactions, prev_hash)
        self.pending_transactions.clear()
        proof = self.get_proof(new_block)
        new_block.add_proof(proof)
        self.chain.append(new_block)
        return

    def get_proof(self, block):
        str_repr = block.str_repr()
        target = "0" * self.diff_level
        proof = 0
        while(not self.is_valid_proof(str_repr, proof, target)):
            proof += 1
        return proof

    def is_valid_proof(self, str_repr, proof, target):
        guess_string = str_repr + str(proof)
        guess_string = guess_string.encode()
        guess_hash = sha256(guess_string).hexdigest()
        return guess_hash[:self.diff_level] == target

    def show_chain(self):
        for block in self.chain:
            print(f"Block: {block.index}")
            for transaction in block.transactions:
                print(f"\tTransaction -> sender: {transaction.sender}, receiver: {transaction.receiver}, amount: {transaction.amount}")
            print("=======================================")
        return

transactions = [
    Transaction('joe', 'amy', 100),
    Transaction('steve', 'barney', 50),
    Transaction('bethany', 'ash', 25),
    Transaction('hady', 'shady', 10),
    Transaction('moe', 'homer', 60)
]

def main():
    bc = BlockChain()
    bc.add_transaction(transactions[0])
    bc.add_transaction(transactions[1])
    bc.create_block()
    bc.add_transaction(transactions[2])
    bc.add_transaction(transactions[3])
    bc.create_block()
    bc.add_transaction(transactions[4])
    bc.create_block()

    bc.show_chain()
    return

if __name__=='__main__':
    main()