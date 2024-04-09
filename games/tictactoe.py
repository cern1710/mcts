from board import Board
from typing import List, Optional, Set

class TicTacToeBoard(Board):
    def __init__(self):
        super().__init__()
        self.space: List[List[Optional[bool]]] = [[None, None, None]
                                                  for _ in range(3)]

    def deep_copy(self) -> 'TicTacToeBoard':
        copy = TicTacToeBoard()
        copy.space = [row[:] for row in self.space]
        copy.terminal = self.terminal
        copy.winner = self.winner
        copy.turn = self.turn
        return copy

    def find_successors(self) -> Set['TicTacToeBoard']:
        successors = set()
        if self.terminal:
            return successors
        # TODO: add this lol
        return successors

    def find_rand_successor(self) -> Optional['TicTacToeBoard']:
        if self.terminal:
            return None
        # TODO: complete this lol
        return None

    def is_terminal(self) -> bool:
        return self.terminal

    def get_reward(self) -> float:
        if not self.terminal:
            return 0.0  # Game has not finished
        if self.winner is None:
            return 0.5  # Draw
        return 1.0 if (self.winner == self.turn) else 0.0