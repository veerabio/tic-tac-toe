from board import Board


class Game:

    def __init__(self, board_printer):
        self.__board = Board(3)
        self.__board_printer = board_printer
        self.__x_turn = True

    def who_won(self):
        # horizontals
        for x in range(self.__board.size):
            if self.__board[x, 0] == self.__board[x, 1] and self.__board[x, 1] == self.__board[x, 2]:
                return self.__board[x, 0]

        # Verticals
        for y in range(self.__board.size):
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
        for x in range(self.__board.size):
            for y in range(self.__board.size):
                if self.__board[x, y] is None:
                    return False
        return True

    def print_board(self):
        self.__board_printer.print_board(self.__board)

    def prompt(self, who):
        while True:
            user_sel = self.__board_printer.get_selection(who)
            if self.__board[user_sel] is None:
                return user_sel
            self.__board_printer.print_invalid_selection()

    def set_selection(self, sel, who):
        self.__board[sel] = who

    def run(self):
        while not self.has_winner() and not self.cats_game():
            self.print_board()

            # Prompt user to select a square
            whose_turn = "X's" if self.__x_turn else "O's"
            selection = self.prompt(whose_turn)

            # record their selection
            self.set_selection(selection, self.__x_turn)

            self.__x_turn = not self.__x_turn  # next players turn

        self.print_board()
        winner = self.who_won()
        if winner is None:
            self.__board_printer.print_cats_game()
        else:
            winner = "X" if winner else "O"
            self.__board_printer.print_winner(winner)
