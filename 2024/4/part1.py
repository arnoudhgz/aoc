from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

count = 0
grid = []
with open(file_name, 'r') as file:
    for line in file:
        grid.append(line.replace("\n", ""))

matrix = [list(row) for row in grid]

# Define the target string
target = "XMAS"
target_len = len(target)

# Function to check diagonals in four directions, horizontals in two directions, and verticals
def find_matching_patterns(matrix, target):
    matches = []

    rows = len(matrix)
    cols = len(matrix[0])

    # Check diagonals starting from every position in the matrix
    for row in range(rows):
        for col in range(cols):
            # Check diagonal top-left to bottom-right (↘)
            if row + target_len <= rows and col + target_len <= cols:
                if all(matrix[row + i][col + i] == target[i] for i in range(target_len)):
                    matches.append((row, col, '↘'))

            # Check diagonal top-right to bottom-left (↙)
            if row + target_len <= rows and col - target_len + 1 >= 0:
                if all(matrix[row + i][col - i] == target[i] for i in range(target_len)):
                    matches.append((row, col, '↙'))

            # Check diagonal bottom-left to top-right (↗)
            if row - target_len + 1 >= 0 and col + target_len <= cols:
                if all(matrix[row - i][col + i] == target[i] for i in range(target_len)):
                    matches.append((row, col, '↗'))

            # Check diagonal bottom-right to top-left (↖)
            if row - target_len + 1 >= 0 and col - target_len + 1 >= 0:
                if all(matrix[row - i][col - i] == target[i] for i in range(target_len)):
                    matches.append((row, col, '↖'))

            # Check horizontal left to right (→)
            if col + target_len <= cols:
                if all(matrix[row][col + i] == target[i] for i in range(target_len)):
                    matches.append((row, col, '→'))

            # Check horizontal right to left (←)
            if col - target_len + 1 >= 0:
                if all(matrix[row][col - i] == target[i] for i in range(target_len)):
                    matches.append((row, col, '←'))

            # Check vertical top to bottom (↓)
            if row + target_len <= rows:
                if all(matrix[row + i][col] == target[i] for i in range(target_len)):
                    matches.append((row, col, '↓'))

            # Check vertical bottom to top (↑)
            if row - target_len + 1 >= 0:
                if all(matrix[row - i][col] == target[i] for i in range(target_len)):
                    matches.append((row, col, '↑'))

    return matches

# Find all matching patterns for "XMAS"
matches = find_matching_patterns(matrix, target)

print(f"Total matches: {len(matches)}")