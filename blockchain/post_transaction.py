import requests
import json
import datetime

from participant import Participant

def main(sender, receiver, amount, description, url):
    time = datetime.datetime.now().isoformat()

    transaction_unsigned = {
        "time"          : time,
        "sender"        : sender.get_public_key().to_string().hex(),
        "receiver"      : receiver.get_public_key().to_string().hex(),
        "amount"        : amount,
        "description"   : description
    }

    signature_str = signature(transaction_unsigned, sender.get_secret_key())

    transaction = {
        "time": time,
        "sender": sender.get_public_key().to_string().hex(),
        "receiver": receiver.get_public_key().to_string().hex(),
        "amount": amount,
        "description": description, 
        "signature": signature_str
    }

    res = requests.post(url, json.dumps(transaction))
    print(res.json())

def signature(transaction_unsigned, secret_key):
    transaction_json = json.dumps(transaction_unsigned)
    transaction_bytes = bytes(transaction_json, encoding = "utf-8")
    signature = secret_key.sign(transaction_bytes)
    signature_str = signature.hex()
    return signature_str

if __name__ == "__main__":
    url = "http://127.0.0.1:8003/transaction_pool/"
    sender = Participant("C")
    receiver = Participant("A")
    amount = 222
    description = "Fee from C-san to A-san"

    main(sender, receiver, amount, description, url)