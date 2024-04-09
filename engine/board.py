from node import Node
from typing import Optional

class Board(Node):
    def __init__(self):
        self.terminal: bool = False
        self.winner: Optional[bool] = None
        self.turn: bool = True

    def print_board(self) -> None:
        return None

    def is_terminal(self) -> bool:
        return self.terminal