from game import Game
from board_printer import BoardPrinter

if __name__ == "__main__":
    game = Game(BoardPrinter())
    game.run()
