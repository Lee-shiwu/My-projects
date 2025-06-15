# player.py
from typing import Tuple

class HumanPlayer:
    """Human player: reads row/column input from the console."""

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def get_move(self) -> Tuple[int, int]:
        """
        Prompts the user to enter "row col", e.g. "1 2" for row 2, column 3.
        Returns zero-based indices (row, col).
        """
        while True:
            try:
                raw = input(f"Player {self.symbol}, enter your move (row col): ")
                row_str, col_str = raw.strip().split()
                row, col = int(row_str) - 1, int(col_str) - 1
                if row in range(3) and col in range(3):
                    return row, col
                else:
                    print("Out of range—please enter numbers 1 through 3.")
            except ValueError:
                print("Invalid format—please input two numbers like “2 3”.")
