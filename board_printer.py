import sys


class BoardPrinter:
    def __init__(self):
        self.columns = ["A", "B", "C"]
        self.mapping = {
            "A": 0,
            "B": 1,
            "C": 2
        }

    def print_board(self, board):
        print("")
        for r in range(board.size):
            for c in range(board.size):
                who = board[r, c]
                if who is None:
                    print(f" {self.columns[c]}{r} ", end='')
                elif who:
                    print("  X ", end='')
                else:
                    print("  O ", end='')
            print("")

    def get_selection(self, who):
        sys.stdout.write(f"{who} turn, select a square (e.g. A0, B2, C1):")
        selection = input()
        # Must be a 2 character string
        if len(selection) is 2:
            col = selection[0:1].upper()
            row = selection[1:]

            # Must be A, B, C and 0, 1, 2
            if col in ["A", "B", "C"] and row in ["0", "1", "2"]:
                col = self.mapping[col]
                row = int(row)
                return row, col
        return None

    @staticmethod
    def print_invalid_selection():
        print("Invalid selection, try again...")

    @staticmethod
    def print_cats_game():
        print("")
        print("Aw, bummer. Cat's game. Meow!")

    @staticmethod
    def print_winner(winner):
        print("")
        print(f"Huzzah! {winner} won!")
