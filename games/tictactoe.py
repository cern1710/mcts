from board import Board
from typing import List, Optional, Set, Tuple
import random

class TicTacToeBoard(Board):
    BOARD_SIZE = 3
    EMPTY = None
    WIN_LINES = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def __init__(self):
        super().__init__()
        self.space: List[List[Optional[bool]]] = [
            [self.EMPTY, self.EMPTY, self.EMPTY] for _ in range(self.BOARD_SIZE)
        ]

    def _deep_copy(self) -> 'TicTacToeBoard':
        copy = TicTacToeBoard()
        copy.terminal = self.terminal
        copy.winner = self.winner
        copy.turn = self.turn
        copy.space = [row[:] for row in self.space]
        return copy

    def _check_win(self) -> Optional[bool]:
        for line in self.WIN_LINES:
            values = [self.space[x][y] for x, y in line]
            if values in ([True, True, True], [False, False, False]):
                return values[0]
        return

    def _update_state(self) -> None:
        winner = self._check_win()
        if winner is not None:
            self.terminal = True
            self.winner = winner
        elif all(cell is not self.EMPTY for row in self.space for cell in row):
            self.terminal = True  # Draw
        else:
            self.turn = not self.turn  # Game has not ended

    def find_successors(self) -> Set['TicTacToeBoard']:
        successors: Set['TicTacToeBoard'] = set()
        if self.terminal:
            return successors
        for i in range(3):
            for j in range(3):
                if self.space[i][j] is not self.EMPTY:
                    continue
                succ = self._deep_copy()
                succ.space[i][j] = self.turn
                succ._update_state()
                successors.add(succ)
        return successors

    def find_next_successor(self) -> Optional['TicTacToeBoard']:
        empty_cells: List[Tuple[int, int]] = [(i, j) for j in range(3)
                       for i in range(3) if self.space[i][j] is self.EMPTY]
        if not empty_cells:
            self.terminal = True  # Terminate game if all cells are filled
            return
        move: Tuple[int, int] = random.choice(empty_cells)
        succ = self._deep_copy()
        succ.space[move[0]][move[1]] = self.turn
        succ._update_state()
        return succ

    def get_reward(self) -> float:
        if not self.terminal:
            return 0.0  # Game has not finished
        if self.winner is None:
            return 0.5  # Draw
        return 1.0 if (self.winner == self.turn) else 0.0

    def print_board(self) -> None:
        symbols = {True: 'X', False: 'O', None: ' '}
        print('-' * 13)
        for row in self.space:
            print('| ',end="")
            print(' | '.join(symbols[cell] for cell in row),end="")
            print(' |')
            print('-' * 13)

    def __eq__(self, other: 'TicTacToeBoard'):
        return isinstance(other, TicTacToeBoard) and self.space == other.space

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.space))