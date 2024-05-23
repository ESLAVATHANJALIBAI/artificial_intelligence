import heapq

class PuzzleState:
    def __init__(self, board, empty_pos, g_cost=0, f_cost=0, parent=None):
        self.board = board
        self.empty_pos = empty_pos
        self.g_cost = g_cost
        self.f_cost = f_cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def heuristic(board, goal):
    # Manhattan distance as the heuristic function
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_x, goal_y = divmod(goal.index(board[i][j]), 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = state.empty_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in state.board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            neighbors.append(PuzzleState(new_board, (new_x, new_y), state.g_cost + 1))
    
    return neighbors

def a_star_search(start_board, goal_board):
    goal = sum(goal_board, [])
    start = PuzzleState(start_board, next((i, j) for i, row in enumerate(start_board) for j, val in enumerate(row) if val == 0))
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {tuple(map(tuple, start_board)): None}
    g_cost = {tuple(map(tuple, start_board)): 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current.board == goal_board:
            path = []
            while current:
                path.append(current.board)
                current = current.parent
            return path[::-1]
        
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(map(tuple, neighbor.board))
            tentative_g_cost = current.g_cost + 1

            if neighbor_tuple not in g_cost or tentative_g_cost < g_cost[neighbor_tuple]:
                g_cost[neighbor_tuple] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor.board, goal)
                neighbor.f_cost = f_cost
                neighbor.parent = current
                heapq.heappush(open_set, (f_cost, neighbor))
    
    return None

def print_board(board):
    for row in board:
        print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))
    print()

# Example usage
start_board = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

path = a_star_search(start_board, goal_board)
if path:
    print("Path to solve the puzzle:")
    for board in path:
        print_board(board)
else:
    print("No solution found")
