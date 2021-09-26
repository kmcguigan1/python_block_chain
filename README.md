# python_block_chain
This repository is a python implementation of the proof of work algorithm in a simulated blockchain of transactions.

## Motivation
This repository is meant to be a place to learn about the principals of hashing as well as the proof of work algorithm inplemented in blockchain technologies.

## Results

Given these transactions;

```
transactions = [
    Transaction('joe', 'amy', 100),
    Transaction('steve', 'barney', 50),
    Transaction('bethany', 'ash', 25),
    Transaction('hady', 'shady', 10),
    Transaction('moe', 'homer', 60)
]
```

Produces the following block;

```
==============================================================================
Block: 1
Timestamp: 1632692793.0655887
Previous hash: 1
Proof: 53578
==============================================================================
Block: 2
Timestamp: 1632692793.1543298
Previous hash: 0000df25d4724b01ee9a367ac5c359eccf2c884a1cad8fd3c8787f9535650558
Proof: 88995

        Transaction -> sender: joe, receiver: amy, amount: 100
        Transaction -> sender: steve, receiver: barney, amount: 50
==============================================================================
Block: 3
Timestamp: 1632692793.3288631
Previous hash: 0000c4425124e4e2ef3c20536d63d542035ee7696f39021a09dd61a2c699d395
Proof: 21738

        Transaction -> sender: bethany, receiver: ash, amount: 25
        Transaction -> sender: hady, receiver: shady, amount: 10
==============================================================================
Block: 4
Timestamp: 1632692793.3717487
Previous hash: 0000fea638b1b67b198ce3c1c61916052e34a2e85546b3d4586cc1b6aef8ffb6
Proof: 53110

        Transaction -> sender: moe, receiver: homer, amount: 60
==============================================================================
```
