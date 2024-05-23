import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

# Function to check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to evaluate the board
def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1 or is_full(board):
        return score

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Initial board:")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'O'
        print("Board after your move:")
        print_board(board)

        if check_winner(board) == 'O':
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI's move
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'
        print("Board after AI's move:")
        print_board(board)

        if check_winner(board) == 'X':
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()

