from typing import Tuple

class TicTacToeBoard(Board):
    def __init__(self):
        super().__init__()
        self.space = Tuple((None, None, None),
                      (None, None, None),
                      (None, None, None))