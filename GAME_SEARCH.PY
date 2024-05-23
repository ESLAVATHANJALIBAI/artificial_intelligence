def is_safe(board, row, col, N):
    # Check the column for any conflicts
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens_util(board, row, N):
    # If all queens are placed successfully
    if row >= N:
        return True
    
    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1
            
            # Recur to place the rest of the queens
            if solve_n_queens_util(board, row + 1, N):
                return True
            
            # If placing queen in board[row][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[row][col] = 0
    
    # If the queen cannot be placed in any column in this row, return False
    return False

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return
    
    # Print the solution
    print_board(board)

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

# Example usage
N = 8
solve_n_queens(N)
