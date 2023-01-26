from pydantic import BaseModel
from typing import List

from transaction import Transaction

class Block(BaseModel):
    time            : str
    transactions    : List[Transaction]
    hash            : str
    nonce           : int