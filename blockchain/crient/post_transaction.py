import requests
import json
import datetime

def main():
    time = datetime.datetime.now().isoformat()

    sender = "sender1"
    receiver = "receiver1"
    amount = 1000
    discription = "demo transaction1"
    signature = "signature sample1"

    transaction = {
        "time": time,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "description": discription,
        "signature": signature
    }

    url ="http://127.0.0.1:8001/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))
    print(res.json())

    sender = "sender2"
    receiver = "receiver2"
    amount = 2000
    discription = "demo transaction2"
    signature = "signature sample2"

    transaction = {
        "time": time,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "description": discription,
        "signature": signature
    }

    url ="http://127.0.0.1:8002/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))
    print(res.json())

    sender = "sender3"
    receiver = "receiver3"
    amount = 3000
    discription = "demo transaction3"
    signature = "signature sample3"

    transaction = {
        "time": time,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "description": discription,
        "signature": signature
    }

    url ="http://127.0.0.1:8003/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))
    print(res.json())

if __name__ == "__main__":
    main()