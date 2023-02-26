import os
from cryptographic_key import CryptographicKey

dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "participants")

class Participant(object):
    """
    ブロックチェーンの参加者を管理するクラス
    """
    def __init__(self, name: str):
        file_name = name + ".txt"
        participants_path = os.path.join(dir_path, file_name)

        self.key = CryptographicKey()

        if os.path.exists(participants_path):
            with open(participants_path, "r") as file:
                secret_key_str = file.read()

            self.key.load_key(secret_key_str)
        
        else:
            self.key.generate_key()

            with open(participants_path, "w") as file:
                file.write(self.key.get_secret_key().to_string().hex())
    
    def get_secret_key(self):
        return self.key.get_secret_key()
    
    def get_public_key(self):
        return self.key.get_public_key()