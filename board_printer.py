class BoardPrinter:

    @staticmethod
    def print_board(board):
        print("")
        for r in range(board.rows):
            for c in range(board.columns):
                who = board[r, c]
                if who is None:
                    print(" - ", end='')
                elif who:
                    print(" X ", end='')
                else:
                    print(" O ", end='')
            print("")
