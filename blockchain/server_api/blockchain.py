import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transaction import Transaction

class BlockChain(object):
    """
    ブロックチェーンの構造や機能を含んだクラス
    """
    def __init__(self):
        self.transaction_pool = {"transactions": []}
        self.block = {"blocks": []}
    
    def add_transaction_pool(self, Transaction):
        transaction_dict = Transaction.dict()
        self.transaction_pool["transactions"].append(transaction_dict)