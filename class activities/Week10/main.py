# main.py
from game import TicTacToe

def main() -> None:
    print("=== Welcome to Tic-Tac-Toe ===")
    game = TicTacToe()
    game.start()

if __name__ == "__main__":
    main()
