import os
import sys
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
        self.REWORD_AMOUNT = 12.5
    
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