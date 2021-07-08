from class_definitions.BlockChain import BlockChain
from class_definitions.Transaction import Transaction

test_transactions = [
    Transaction("Bob", "Alice", "10"),
    Transaction("Alice", "Charlie", "10"),
    Transaction("Charlie", "Bob", "10"),
]

def test_single_block():
    print("\ntest_single_block")
    block_chain = BlockChain()
    for transaction in test_transactions:
        block_chain.add_transaction(transaction)
    block_chain.mine_block()
    print("After")
    block_chain.show_chain()
    return
    
def test_single_transaction_blocks():
    print("\ntest_single_transaction_blocks")
    block_chain = BlockChain()
    for transaction in test_transactions:
        block_chain.add_transaction(transaction)
        block_chain.mine_block()
    print("After")
    block_chain.show_chain()
    return    

def test_multiple_blocks():
    print("\ntest_multiple_blocks")
    block_chain = BlockChain()
    for i, transaction in enumerate(test_transactions):
        block_chain.add_transaction(transaction)
        if(i == 1):
            block_chain.mine_block()
    block_chain.mine_block()
    print("After")
    block_chain.show_chain()
    return   

def main():
    test_single_block()
    test_single_transaction_blocks()
    test_multiple_blocks()
    return

if __name__ == "__main__":
    main()