class BlockChain(object):
    """
    ブロックチェーンの構造や機能を含んだクラス
    """
    def __init__(self):
        self.transaction_pool = {"transactions": []} # ジェネシスブロック
    
