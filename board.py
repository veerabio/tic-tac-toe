class Board:
    def __init__(self):
        # X = True
        # O = False
        # Empty = None
        self.__game_board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

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
