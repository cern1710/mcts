from node import Node
from typing import Optional, List

class Board(Node):
    def __init__(self):
        self.terminal: bool = False
        self.winner: Optional[bool] = None
        self.turn: bool = True
        self.space: List[List[Optional[bool]]] = list()

    def print_board(self) -> None:
        return

    def __eq__(self, other: 'Board'):
        return isinstance(other, Board) and self.space == other.space

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.space))