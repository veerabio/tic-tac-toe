from game import Game

if __name__ == "__main__":
    # X = True
    # O = False
    # Empty = None
    game = Game()

    x_turn = True

    while not game.has_winner() and not game.cats_game():
        game.print_board()

        # Prompt user to select a square
        whose_turn = "X's" if x_turn else "O's"
        selection = game.prompt(whose_turn)

        # record their selection
        game.set_selection(selection, x_turn)

        x_turn = not x_turn # next players turn

    game.print_board()
    winner = game.who_won()
    if winner is None:
        print("")
        print("Aw, bummer. Cat's game. Meow!")
    else:
        winner = "X" if winner else "O"
        print("")
        print(f"Huzzah! {winner} won!")
