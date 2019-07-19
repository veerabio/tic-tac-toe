import sys
from board import Board
from board_printer import BoardPrinter


class Game:

    def __init__(self):
        self.__board = Board()

    def who_won(self):
        # horizontals
        for x in range(self.__board.columns):
            if self.__board[x, 0] == self.__board[x, 1] and self.__board[x, 1] == self.__board[x, 2]:
                return self.__board[x, 0]

        # Verticals
        for y in range(self.__board.rows):
            if self.__board[0, y] == self.__board[1, y] and self.__board[1, y] == self.__board[2, y]:
                return self.__board[0, y]

        # Diagonals
        if self.__board[0, 0] == self.__board[1, 1] and self.__board[1, 1] == self.__board[2, 2]:
            return self.__board[0, 0]
        if self.__board[2, 0] == self.__board[1, 1] and self.__board[1, 1] == self.__board[0, 2]:
            return self.__board[2, 0]
        return None

    def has_winner(self):
        return self.who_won() is not None

    def cats_game(self):
        # Check if any space on the board is still empty
        for x in range(3):
            for y in range(3):
                if self.__board[x, y] is None:
                    return False
        return True

    def print_board(self):
        BoardPrinter.print_board(self.__board)

    def prompt(self, who):
        while True:
            sys.stdout.write(f"{who} turn, select a square (e.g. A0, B2, C1):")
            user_sel = self.__board.selection_to_row_col(input())
            if user_sel:
                return user_sel
            print("Invalid selection, try again...")
        return None

    def set_selection(self, sel, who):
        self.__board[sel] = who
