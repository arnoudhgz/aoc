from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

grid = []
with open(file_name, 'r') as file:
    for line in file:
        grid.append(line.strip())

matrix = [[int(value) for value in row] for row in grid]

from collections import deque

# Function to count distinct hiking trails starting from a trailhead
def count_distinct_trails(map, start):
    rows, cols = len(map), len(map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # DFS function to explore all valid paths
    def dfs(x, y, visited):
        # If we reach height 9, it's a valid trail
        if map[x][y] == 9:
            return 1

        trail_count = 0

        # Explore all four directions (up, down, left, right)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Ensure we are within bounds and the move is valid
            if 0 <= nx < rows and 0 <= ny < cols and map[nx][ny] == map[x][y] + 1:
                if (nx, ny) not in visited:  # Track visited positions per trail
                    visited.add((nx, ny))  # Mark this position as visited for the current path
                    trail_count += dfs(nx, ny, visited)  # Continue DFS from this position
                    visited.remove((nx, ny))  # Unmark position after exploring

        return trail_count

    # Start DFS from the trailhead
    visited = set()
    visited.add(start)
    return dfs(start[0], start[1], visited)

# Function to calculate the sum of ratings for all trailheads
def calculate_ratings(map):
    rows, cols = len(map), len(map[0])
    total_rating = 0

    # Traverse the map to find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 0:
                # For each trailhead, calculate the number of distinct hiking trails
                rating = count_distinct_trails(map, (i, j))
                total_rating += rating

    return total_rating

# Calculate and print the total rating of all trailheads
total_rating = calculate_ratings(matrix)
print("Total rating of all trailheads:", total_rating)





