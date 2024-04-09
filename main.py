import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "games"))
sys.path.append(os.path.join(current_dir, "engine"))
from games import game_engines

if __name__ == "__main__":
    weight = 0.01
    rollout = 500
    display = False

    iter = 20
    total = [0] * 3

    for _ in range(iter):
        res = game_engines.tictactoe_engine(weight, rollout, display)
        total[res] += 1

    print(f"Draws: {total[0]}")
    print(f"X wins: {total[1]}")
    print(f"O wins: {total[2]}")