def print_board(board):
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(" " + cell + " ", end="|")
        print("\n-------------")


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
