import sys
import os

sys.path.append(os.path.abspath("engine"))
sys.path.append(os.path.abspath("games"))
from mcts import MCTS, Node

if __name__ == "__main__":
    tree = MCTS()
