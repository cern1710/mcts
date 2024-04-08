from node import Node
from typing import Tuple

class Board(Node):
    def __init__(self):
        self.terminal = False
        self.winner = None
        self.turn = True
        self.space = Tuple()