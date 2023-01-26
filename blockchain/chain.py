from pydantic import BaseModel
from typing import List

from block import Block

class Chain(BaseModel):
    blocks  : List[Block]