from collections import deque

def water_jug_bfs(m, n, d):
    # m: capacity of first jug
    # n: capacity of second jug
    # d: target amount of water to measure

    # Initialize the queue for BFS
    queue = deque([(0, 0)])  # (amount_in_jug1, amount_in_jug2)
    
    # Set to keep track of visited states
    visited = set((0, 0))

    # List to keep the path/steps to reach the target
    path = []

    while queue:
        jug1, jug2 = queue.popleft()
        
        # Append the current state to the path
        path.append((jug1, jug2))

        # Check if we have reached the solution
        if jug1 == d or jug2 == d:
            return path

        # Generate all possible next states
        next_states = set()

        # Fill jug1
        next_states.add((m, jug2))

        # Fill jug2
        next_states.add((jug1, n))

        # Empty jug1
        next_states.add((0, jug2))

        # Empty jug2
        next_states.add((jug1, 0))

        # Pour water from jug1 to jug2
        pour_to_jug2 = min(jug1, n - jug2)
        next_states.add((jug1 - pour_to_jug2, jug2 + pour_to_jug2))

        # Pour water from jug2 to jug1
        pour_to_jug1 = min(jug2, m - jug1)
        next_states.add((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

        # Process each next state
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    # If no solution is found
    return "No solution found"

# Example usage
m = 3  # Capacity of the first jug
n = 5  # Capacity of the second jug
d = 4  # Target amount of water

solution_path = water_jug_bfs(m, n, d)
print("Steps to measure the target amount of water:")
for step in solution_path:
    print(step)
