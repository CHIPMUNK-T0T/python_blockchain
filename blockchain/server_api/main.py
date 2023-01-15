import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from blockchain import BlockChain
from transaction import Transaction

app = FastAPI()
blockchain = BlockChain()

@app.get("/transaction_pool")
def get_transaction():
    """
    トランザクションプールをブラウザ上に表示させる
    """
    return blockchain.transaction_pool

@app.get("/chain")
def get_chain():
    """チェーンをブラウザに表示させる
    """
    return blockchain.block

@app.post("/transaction_pool")
def post_transaction_pool(transaction :Transaction):
    """
    トランザクションをトランザクションプールに追加する
    """
    blockchain.add_transaction_pool(transaction)
    return { "message" : "Transaction is posted."}

@app.post("/create_chain")
def create_chain():
    """
    ブロックの生成処理を行う
    """
    pass