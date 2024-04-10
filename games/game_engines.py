from mcts import MCTS
from opt_tictactoe import TicTacToeBoard
import random

def parse_input(game_board: TicTacToeBoard) -> TicTacToeBoard:
    valid_move = False
    while not valid_move:
        try:
            user_move = input("Enter your move (row,col): ")
            row, col = map(int, user_move.split(','))
            pos = (row - 1) * 3 + (col - 1)
            if game_board.is_valid_move(pos):
                game_board._update_state(pos)
                valid_move = True
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid format. Please enter row and column as 'row,col'.")
    return game_board

def random_player_move(game_board: TicTacToeBoard) -> TicTacToeBoard:
    valid_moves = [i for i in range(9) if game_board.is_valid_move(i)]
    if not valid_moves:
        return game_board
    move = random.choice(valid_moves)
    game_board._update_state(move)
    return game_board

def tictactoe_engine(weight: float,
                     rollout: int,
                     display=True,
                     player=False) -> int:
    game_board = TicTacToeBoard()
    mcts = MCTS(weight=weight)
    turn = 0

    if player == True:
        if display == True:
            if (random.randint(0, 1) == 0):
                print("You are 'O'! AI makes the first move.")
            else:
                print("You are 'X'! You makes the first move.")
                # turn = 1
        turn = 1

    if display == True:
        print("Tic Tac Toe game started. Player 'X' makes the first move!")

    while not game_board.is_terminal():
        if turn % 2 == 1:
            next_move = parse_input(game_board)
            # next_move = random_player_move(game_board)
            game_board = next_move
        else:
            for _ in range(rollout):
                mcts.rollout(game_board)

            if game_board.terminal:
                break

            # Select move with the highest visit count
            next_move = max(game_board.find_successors(), key=lambda node: mcts.N[node])
            game_board = next_move

        if player == True:
            turn += 1

        if display == True:
            game_board.print_board()
            if not game_board.is_terminal():
                print(f"\nPlayer {'X' if game_board.turn else 'O'} makes a move.")

    if display == True:
        if game_board.winner is None:
            print("\nThe game is a draw!")
        else:
            print(f"\nPlayer {'X' if game_board.winner else 'O'} wins!")

    if game_board.winner is None:
        return 0
    else:
        return 1 if game_board.winner else 2