from ecdsa import SigningKey
from ecdsa import SECP256k1
import binascii

class CryptographicKey(object):
    """
    公開鍵暗号による鍵の生成を行う。
    """
    def __init__(self):
        self.has_key = False
    
    def generate_key(self):
        if not self.has_key:
            self.secret_key = SigningKey.generate(curve=SECP256k1)
            self.public_key = self.secret_key.verifying_key

            self.has_key = True
    
    def load_key(self, secret_key_str):
        if not self.has_key:
            self.secret_key = SigningKey.from_string(binascii.unhexlify(secret_key_str), curve=SECP256k1)
            self.public_key = self.secret_key.verifying_key

            self.has_key = True
    
    def get_secret_key(self):
        return self.secret_key
    
    def get_public_key(self):
        return self.public_key