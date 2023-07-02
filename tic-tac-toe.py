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

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
        
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a tie
    if all(cell != " " for row in board for cell in row):
        return "Tie"

    return None


def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"
    winner = None

    while not winner:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the row and column from the current player
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if board[row][col] == " ":
                board[row][col] = current_player
                break
            else:
                print("That cell is already occupied. Try again.")

        # Check for a winner
        winner = check_winner(board)

        # Switch players
        current_player = "O" if current_player == "X" else "X"

    # Print the final board
    print_board(board)

    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")


# Start the game

play_game()

