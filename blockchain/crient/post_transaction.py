import requests
import json
import datetime

def main():
    time = datetime.datetime.now().isoformat()

    sender = "sender"
    receiver = "receiver"
    amount = 1000
    discription = "demo transaction"
    signature = "signature sample"

    transaction = {
        "time": time,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "description": discription,
        "signature": signature
    }

    url ="http://127.0.0.1:8000/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))
    print(res.json())

if __name__ == "__main__":
    main()