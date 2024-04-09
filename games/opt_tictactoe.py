from board import Board
from typing import Optional, Set
import random

class TicTacToeBoard(Board):
    """Optimised Tic Tac Toe board using bit representation of board"""
    WIN_STATES = [
        # Rows
        0b111000000,
        0b000111000,
        0b000000111,
        # Columns
        0b100100100,
        0b010010010,
        0b001001001,
        # Diagonals
        0b100010001,
        0b001010100,
    ]
    END_STATE = 0b111111111

    def __init__(self):
        super().__init__()
        # Initialise bitboards for both players
        self.player_X = 0b0
        self.player_O = 0b0

    def _deep_copy(self) -> 'TicTacToeBoard':
        copy = TicTacToeBoard()
        copy.terminal = self.terminal
        copy.winner = self.winner
        copy.turn = self.turn
        copy.player_X = self.player_X
        copy.player_O = self.player_O
        return copy

    def _check_win(self) -> Optional[bool]:
        for win_state in self.WIN_STATES:
            if (self.player_X & win_state) == win_state:
                return True
            if (self.player_O & win_state) == win_state:
                return False

    def _make_move(self, pos:int) -> None:
        if self.turn:
            self.player_X |= 1 << pos
        else:
            self.player_O |= 1 << pos

    def _update_state(self, pos: int) -> None:
        self._make_move(pos)
        winner = self._check_win()
        if winner is not None:
            self.terminal = True
            self.winner = winner
        elif (self.player_X | self.player_O) == self.END_STATE:
            self.terminal = True  # Draw
        else:
            self.turn = not self.turn  # Game has not ended

    def find_successors(self) -> Set['TicTacToeBoard']:
        successors: Set['TicTacToeBoard'] = set()
        if self.terminal:
            return successors
        occupied = self.player_X | self.player_O
        for pos in range(9):
            if (occupied & (1 << pos)):
                continue
            succ = self._deep_copy()
            succ._update_state(pos)
            successors.add(succ)
        return successors

    def find_rand_successor(self) -> Optional['TicTacToeBoard']:
        occupied = (self.player_X | self.player_O)
        empty_positions = [i for i in range(9) if not (occupied & (1 << i))]
        if not empty_positions:
            self.terminal = True
            return None
        move = random.choice(empty_positions)
        succ = self._deep_copy()
        succ._update_state(move)
        return succ

    def get_reward(self) -> float:
        if not self.terminal:
            return 0.0  # Game has not finished
        if self.winner is None:
            return 0.5  # Draw
        return 1.0 if (self.winner == self.turn) else 0.0

    def print_board(self) -> None:
        row_sep = '-' * 13
        print(row_sep)
        board_str = ''
        for position in range(9):
            if position % 3 == 0:
                board_str += '| '
            if self.player_X & (1 << position):
                board_str += 'X'
            elif self.player_O & (1 << position):
                board_str += 'O'
            else:
                board_str += ' '
            if position % 3 == 2:
                board_str += ' | \n' + row_sep + '\n'
            else:
                board_str += ' | '
        print(board_str)

    def __eq__(self, other):
        return isinstance(other, TicTacToeBoard) \
                and self.player_X == other.player_X \
                and self.player_O == other.player_O

    def __hash__(self):
        return hash((self.player_X, self.player_O))