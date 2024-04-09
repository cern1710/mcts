from mcts import MCTS
from tictactoe import TicTacToeBoard

def tictactoe_engine(weight: float, rollout: int, display=True) -> int:
    game_board = TicTacToeBoard()
    mcts = MCTS(weight=weight)

    if display == True:
        print("Tic Tac Toe game started. Player 'X' makes the first move!")

    while not game_board.is_terminal():
        for _ in range(rollout):
            mcts.rollout(game_board)

        # Select move with the highest visit count
        next_move = max(game_board.find_successors(), key=lambda node: mcts.N[node])
        game_board = next_move

        if display == True:
            game_board.print_board()
            if not game_board.is_terminal():
                print(f"\nPlayer {'X' if game_board.turn else 'O'} made a move.")

    if display == True:
        if game_board.winner is None:
            print("\nThe game is a draw!")
        else:
            print(f"\nPlayer {'X' if game_board.winner else 'O'} wins!")

    if game_board.winner is None:
        return 0
    else:
        return 1 if game_board.winner else 2