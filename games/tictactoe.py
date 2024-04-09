from board import Board
from typing import List, Optional, Set, Tuple
import random

class TicTacToeBoard(Board):
    def __init__(self):
        super().__init__()
        self.space: List[List[Optional[bool]]] = [[None, None, None]
                                                  for _ in range(3)]

    def _deep_copy(self) -> 'TicTacToeBoard':
        copy = TicTacToeBoard()
        copy.terminal = self.terminal
        copy.winner = self.winner
        copy.turn = self.turn
        copy.space = [row[:] for row in self.space]
        return copy

    def _update_state(self):
        # TODO: check if win or not
        self.turn = not self.turn

    def find_successors(self) -> Set['TicTacToeBoard']:
        successors: Set['TicTacToeBoard'] = set()
        if self.terminal:
            return successors
        for i in range(3):
            for j in range(3):
                if self.space[i][j] is not None:
                    continue
                succ = self._deep_copy()
                succ.space[i][j] = self.turn
                succ._update_state()
                successors.add(succ)
        return successors

    def find_rand_successor(self) -> Optional['TicTacToeBoard']:
        if self.terminal:
            return None
        empty_cells: List[Tuple[int, int]] = [(i, j) for j in range(3)
                       for i in range(3) if self.space[i][j]]
        if not empty_cells:
            return None
        move: Tuple[int, int] = random.choice(empty_cells)
        succ = self._deep_copy()
        succ.space[move[0]][move[1]] = self.turn
        succ._update_state()
        return succ

    def is_terminal(self) -> bool:
        return self.terminal

    def get_reward(self) -> float:
        if not self.terminal:
            return 0.0  # Game has not finished
        if self.winner is None:
            return 0.5  # Draw
        return 1.0 if (self.winner == self.turn) else 0.0