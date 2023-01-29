import os
import sys
import json
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transaction import Transaction
import datetime

from ecdsa import VerifyingKey
from ecdsa import SECP256k1
import binascii
import hashlib

class BlockChain(object):
    """
    ブロックチェーンの構造や機能を含んだクラス
    """
    def __init__(self):
        self.transaction_pool = {"transactions": []}
        self.chain = {"blocks": []}
        self.genesis_block = {
            "time": "0000-00-00T00:00:00.000000",
            "transactions": [],
            "hash": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "nonce": 0
        }
        self.server_list = []
        self.REWORD_AMOUNT = 12.5

        self.chain["blocks"].append(self.genesis_block)
    
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

        last_block_dict = self.chain["blocks"][-1]
        hash = self.hash(last_block_dict)

        block = {
            "time": datetime.datetime.now().isoformat(),
            "transactions": transactions,
            "hash": hash,
            "nonce": 0
        }

        self.chain["blocks"].append(block)
        self.transaction_pool["transactions"] = []
    
    def broadcast_transaction(self, transaction):
        transaction_dict = transaction.dict()
        for url in self.server_list:
            res = requests.post(url+"/receive_transaction", json.dumps(transaction_dict))
            print(res.json())
    
    def broadcast_chain(self, chain):
        for url in self.server_list:
            res = requests.post(url+"/receive_chain", json.dumps(chain))
            print(res.json())

    def replace_chain(self, chain):
        self.chain = chain.dict()
        self.transaction_pool["transactions"] = []
    
    def verify_transaction(self, transaction):
        public_key = VerifyingKey.from_string(binascii.unhexlify(transaction.sender), curve=SECP256k1)
        signature = binascii.unhexlify(transaction.signature)

        transaction_unsigned = {
            "time": transaction.time,
            "sender": transaction.sender,
            "receiver": transaction.receiver,
            "amount": transaction.amount,
            "description": transaction.description
        }

        transaction_unsigned_json = json.dumps(transaction_unsigned)
        transaction_unsigned_bytes = bytes(transaction_unsigned_json, encoding = "utf-8")
        return public_key.verify(signature, transaction_unsigned_bytes)

    def hash(self, block_dict):
        block_json = json.dumps(block_dict)
        block_byte = bytes(block_json, encoding="utf-8")
        hash = hashlib.sha256(block_byte).hexdigest()
        return hash