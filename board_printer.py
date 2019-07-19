class BoardPrinter:
    mapping = {
        "A": 0,
        "B": 1,
        "C": 2
    }
    columns = ["A", "B", "C"]

    @staticmethod
    def print_board(board):
        print("")
        for r in range(board.rows):
            for c in range(board.columns):
                who = board[r, c]
                if who is None:
                    print(f" {BoardPrinter.columns[c]}{r} ", end='')
                elif who:
                    print("  X ", end='')
                else:
                    print("  O ", end='')
            print("")

    @staticmethod
    def get_selection():
        selection = input()
        # Must be a 2 character string
        if len(selection) is 2:
            col = selection[0:1].upper()
            row = selection[1:]

            # Must be A, B, C and 0, 1, 2
            if col in ["A", "B", "C"] and row in ["0", "1", "2"]:
                col = BoardPrinter.mapping[col]
                row = int(row)
                return row, col
        return None
