# board.py
from typing import List, Optional

class Board:
    """Board class: maintains a 3×3 grid, provides display, move placement, and win checking."""

    def __init__(self) -> None:
        # Use a space to represent an empty cell
        self.grid: List[List[str]] = [[" "] * 3 for _ in range(3)]

    def display(self) -> None:
        """Prints the current board to the console."""
        for i, row in enumerate(self.grid):
            print(" | ".join(row))
            if i < 2:
                print("---+---+---")

    def place_move(self, row: int, col: int, symbol: str) -> bool:
        """
        Places `symbol` at (row, col).
        Returns True if the move succeeded; False if the cell was already occupied.
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> Optional[str]:
        """
        Checks for a winner: any row, column, or diagonal filled with the same symbol.
        Returns 'X' or 'O' if there is a winner; otherwise returns None.
        """
        lines = []

        # Rows
        lines.extend(self.grid)
        # Columns
        lines.extend([list(col) for col in zip(*self.grid)])
        # Two diagonals
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0] != " " and line.count(line[0]) == 3:
                return line[0]
        return None

    def is_full(self) -> bool:
        """Returns True if there are no empty cells (draw condition)."""
        return all(cell != " " for row in self.grid for cell in row)
