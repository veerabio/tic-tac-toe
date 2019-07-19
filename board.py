class Board:
    def __init__(self, size=3):
        # X = True
        # O = False
        # Empty = None
        self.__size = size
        self.__game_board = [[None for _ in range(size)] for _ in range(size)]

    def __getitem__(self, sel):
        return self.__game_board[sel[0]][sel[1]]

    def __setitem__(self, sel, who):
        self.__game_board[sel[0]][sel[1]] = who

    @property
    def size(self):
        return self.__size
