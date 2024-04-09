import sys
import os
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "games"))
sys.path.append(os.path.join(current_dir, "engine"))
from games import game_engines

if __name__ == "__main__":
    weight = 1e-1
    rollout = 120
    display = False
    player = False

    iter = 500
    total = [0] * 3

    for i in range(iter):
        res = game_engines.tictactoe_engine(weight, rollout, display, player)
        total[res] += 1
        print(f"Current iteration: {i+1}")

    print(f"Draws: {total[0]}")
    print(f"X wins: {total[1]}")
    print(f"O wins: {total[2]}")