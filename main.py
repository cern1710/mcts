import sys
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "games"))
sys.path.append(os.path.join(current_dir, "engine"))
from games import game_engines

if __name__ == "__main__":
    weight = 3e-4
    rollout = 800
    display = False
    player = False

    iter = 100
    total = [0] * 3

    start = time.process_time()
    for i in range(iter):
        res = game_engines.tictactoe_engine(weight, rollout, display, player)
        total[res] += 1
        print(f"Current iteration: {i+1}")
    end = time.process_time() - start

    print(f"Draws: {total[0]}")
    print(f"X wins: {total[1]}")
    print(f"O wins: {total[2]}")
    print(f"Time taken for {iter} iterations: {end}s")