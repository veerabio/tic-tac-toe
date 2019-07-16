import sys


def who_won(board):
    # horizontals
    for x in range(3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2]:
            return board[x][0]

    # Verticals
    for y in range(3):
        if board[0][y] == board[1][y] and board[1][y] == board[2][y]:
            return board[0][y]

    # Diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[2][0]
    return None


def has_winner(board):
    return who_won(board) is not None


def cats_game(board):
    # Check if any space on the board is still empty
    for x in range(3):
        for y in range(3):
            if board[x][y] is None:
                return False
    return True


def print_board(board):
    print("")
    for r in range(3):
        for c in range(3):
            who = board[r][c]
            if who is None:
                print(" - ", end='')
            elif who:
                print(" X ", end='')
            else:
                print(" O ", end='')
        print("")


def set_selection(board, sel, who):
    board[sel[0]][sel[1]] = who


def selection_to_row_col(selection, board):
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
            if board[row][col] is None:
                return (row, col)
    return None


def prompt(who, board):
    while True:
        sys.stdout.write(f"{who} turn, select a square (e.g. A0, B2, C1):")
        user_sel = selection_to_row_col(input(), board)
        if user_sel:
            return user_sel
        print("Invalid selection, try again...")
    return None


if __name__ == "__main__":
    # X = True
    # O = False
    # Empty = None
    game_board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    x_turn = True

    while not has_winner(game_board) and not cats_game(game_board):
        print_board(game_board)

        # Prompt user to select a square
        whose_turn = "X's" if x_turn else "O's"
        selection = prompt(whose_turn, game_board)

        # record their selection
        set_selection(game_board, selection, x_turn)

        x_turn = not x_turn # next players turn

    winner = who_won(game_board)
    if winner is None:
        print("")
        print("Aw, bummer. Cat's game. Meow!")
    else:
        winner = "X" if winner else "O"
        print("")
        print(f"Huzzah! {winner} won!")
