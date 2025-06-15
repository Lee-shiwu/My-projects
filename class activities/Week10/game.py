# game.py
from board import Board
from player import HumanPlayer

class TicTacToe:
    """Game core: handles turns, move processing, win/draw checking."""

    def __init__(self) -> None:
        self.board = Board()
        # Players: X then O
        self.players = [HumanPlayer("X"), HumanPlayer("O")]

    def start(self) -> None:
        """Runs the game loop until someone wins or it’s a draw."""
        current = 0  # 0 → X, 1 → O
        while True:
            self.board.display()
            player = self.players[current]
            row, col = player.get_move()

            if not self.board.place_move(row, col, player.symbol):
                print("That spot is already taken—try again.")
                continue

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"Player {winner} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It’s a draw!")
                break

            # Switch to the other player
            current = 1 - current
