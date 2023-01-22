import os
import sys
import json
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transaction import Transaction
import datetime

class BlockChain(object):
    """
    ブロックチェーンの構造や機能を含んだクラス
    """
    def __init__(self):
        self.transaction_pool = {"transactions": []}
        self.chain = {"blocks": []}
        self.server_list = []
        self.REWORD_AMOUNT = 12.5
    
    def add_server_list(self, server_list):
        self.server_list = server_list

    def add_transaction_pool(self, Transaction):
        transaction_dict = Transaction.dict()
        self.transaction_pool["transactions"].append(transaction_dict)
    
    def create_new_block(self, creator):
        reword_transaction_dict = {
            "time": datetime.datetime.now().isoformat(),
            "sender": "Blockchain",
            "receiver": creator,
            "amount": self.REWORD_AMOUNT,
            "description": "reword",
            "signature": "not need"
        }

        transactions = self.transaction_pool["transactions"].copy()
        transactions.append(reword_transaction_dict)

        block = {
            "time": datetime.datetime.now().isoformat(),
            "transactions": transactions,
            "hash": "hash_sample",
            "nonce": 0
        }

        self.chain["blocks"].append(block)
        self.transaction_pool["transactions"] = []
    
    def broadcast_transaction(self, transaction):
        transaction_dict = transaction.dict()
        for url in self.add_server_list:
            res = requests.post(url+"/receive_transaction", json.dumps(transaction_dict))
            print(res.json())