import math
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    """ Prints the current game board """
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(player):
    """ Checks if the given player ('X' or 'O') has won """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full():
    """ Checks if the board is full (draw) """
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def minimax(is_maximizing):
    """
    Minimax algorithm: Simulates all possible moves and finds the best one.
    Returns +1 if AI (O) wins, -1 if Player (X) wins, and 0 for a draw.
    """
    if is_winner("O"): return 1
    if is_winner("X"): return -1
    if is_full(): return 0

    if is_maximizing:  
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(False)
                    board[row][col] = " "  
                    best_score = max(best_score, score)
        return best_score
    else:  
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(True)
                    board[row][col] = " "  
                    best_score = min(best_score, score)
        return best_score

def best_move():
    """
    Determines the best move for AI ('O') using the Minimax algorithm.
    It evaluates all possible moves and selects the one with the highest Minimax score.
    """
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def play():
    """ Main game loop """
    print("Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.")
    print_board()

    while True:
        # User move
        row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "X"

        print_board()

        if is_winner("X"):
            print("Congratulations! You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = best_move()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        print_board()

        if is_winner("O"):
            print("AI wins! Better luck next time.")
            break
        if is_full():
            print("It's a draw!")
            break
play()
