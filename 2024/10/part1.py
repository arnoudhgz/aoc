from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

grid = []
with open(file_name, 'r') as file:
    for line in file:
        grid.append(line.strip())

matrix = [[int(value) for value in row] for row in grid]

from collections import deque

# Function to perform BFS and count reachable 9's from a trailhead
def count_reachable_nines(map, start):
    rows, cols = len(map), len(map[0])
    visited = set()
    queue = deque([start])
    reachable_nines = 0

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # If we reach height 9, increment the count
        if map[x][y] == 9:
            reachable_nines += 1

        # Explore neighbors with height increase of exactly 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if map[nx][ny] == map[x][y] + 1:
                    queue.append((nx, ny))

    return reachable_nines

# Function to calculate the sum of the scores for all trailheads
def calculate_scores(map):
    rows, cols = len(map), len(map[0])
    total_score = 0

    # Traverse the map to find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 0:
                # For each trailhead, calculate the score (number of reachable 9's)
                score = count_reachable_nines(map, (i, j))
                total_score += score

    return total_score

# Calculate and print the total score of all trailheads
total_score = calculate_scores(matrix)
print("Total score of all trailheads:", total_score)
