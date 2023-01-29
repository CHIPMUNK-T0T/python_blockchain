import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from blockchain import BlockChain
from transaction import Transaction
from chain import Chain

app = FastAPI()
print(app.root_path)
blockchain = BlockChain()

with open("./api_list_3.json") as f:
    api_list = json.load(f)
    blockchain.add_server_list(api_list["server_list"])

@app.get("/transaction_pool")
def get_transaction():
    """
    トランザクションプールをブラウザ上に表示させる
    """
    return blockchain.transaction_pool

@app.get("/chain")
def get_chain():
    """チェーンをブラウザ上に表示させる
    """
    return blockchain.chain

@app.post("/transaction_pool")
def post_transaction_pool(transaction :Transaction):
    """
    トランザクションをトランザクションプールに追加する
    """
    if blockchain.verify_transaction(transaction):
        blockchain.add_transaction_pool(transaction)
        blockchain.broadcast_transaction(transaction)
        return { "message" : "Transaction is posted."}

@app.get("/create_block/{creator}")
def create_block(creator: str):
    """
    ブロックの生成処理を行う
    """
    blockchain.create_new_block(creator)
    blockchain.broadcast_chain(blockchain.chain)
    return {"message": "New Block is Created."}

@app.post("/receive_transaction")
def receive_transaction(transaction :Transaction):
    """
    別のサーバーに追加されたトランザクション情報を受け取る（同期する）
    """
    if blockchain.verify_transaction(transaction):
        blockchain.add_transaction_pool(transaction)
        return { "message" : "Broadcast Transaction is success."}

@app.post("/receive_chain")
def receive_chain(chain: Chain):
    """
    別のサーバーで生成されたブロックを受け取る（同期する）
    """
    if blockchain.verify_chain(chain):
        blockchain.replace_chain(chain)
        return { "message" : "Broadcast Chain is success."}