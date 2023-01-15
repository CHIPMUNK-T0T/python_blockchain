from fastapi import FastAPI

app = FastAPI()

@app.get("/transaction_pool")
def get_transaction():
    """
    トランザクションプールをブラウザ上に表示させる
    """
    pass

@app.get("/chain")
def get_chain():
    """チェーンをブラウザに表示させる
    """
    pass

@app.post("/transaction_pool")
def post_transaction():
    """
    トランザクションをトランザクションプールに追加する
    """
    pass

@app.post("/create_chain")
def create_chain():
    """
    ブロックの生成処理を行う
    """
    pass