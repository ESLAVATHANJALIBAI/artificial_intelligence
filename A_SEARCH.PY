import heapq

def heuristic(a, b):
    # Using Manhattan distance as the heuristic function
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue to hold the nodes to be evaluated
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Dictionaries to keep track of the cost to reach each node and the path
    g_cost = {start: 0}
    came_from = {start: None}
    
    while open_set:
        # Get the node with the lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # If we have reached the goal, reconstruct the path
        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        x, y = current
        
        # Explore neighbors (4 possible movements)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_cost = g_cost[current] + 1
                
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_cost, neighbor))
                    came_from[neighbor] = current

    # If no path found
    return None

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Start position
end = (4, 4)    # End position

path = a_star_search(grid, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")
