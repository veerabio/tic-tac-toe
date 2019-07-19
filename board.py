class Board:
    def __init__(self):
        # X = True
        # O = False
        # Empty = None
        self.__game_board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def selection_to_row_col(self, selection):
        mapping = {
            "A": 0,
            "B": 1,
            "C": 2
        }

        # Must be a 2 character string
        if len(selection) is 2:
            col = selection[0:1].upper()
            row = selection[1:]

            # Must be A, B, C and 0, 1, 2
            if col in ["A", "B", "C"] and row in ["0", "1", "2"]:
                col = mapping[col]
                row = int(row)

                # Make sure that spot is empty
                if self.__game_board[row][col] is None:
                    return row, col
        return None

    def __getitem__(self, sel):
        return self.__game_board[sel[0]][sel[1]]

    def __setitem__(self, sel, who):
        self.__game_board[sel[0]][sel[1]] = who

    @property
    def rows(self):
        return 3

    @property
    def columns(self):
        return 3
