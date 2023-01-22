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
    return blockchain.chain

@app.post("/transaction_pool")
def post_transaction_pool(transaction :Transaction):
    """
    トランザクションをトランザクションプールに追加する
    """
    blockchain.add_transaction_pool(transaction)
    return { "message" : "Transaction is posted."}

@app.get("/create_block/{creator}")
def create_block(creator: str):
    """
    ブロックの生成処理を行う
    """
    blockchain.create_new_block(creator)
    return {"message": "New Block is Created."}