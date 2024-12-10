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
target = "MAS"
target_len = len(target)

# Function to find matching MAS and count repeated row,col positions of "A"
def count_matching_mas(matrix, target):
    matches = []
    rows = len(matrix)
    cols = len(matrix[0])

    # Check diagonals starting from every position in the matrix
    for row in range(rows):
        for col in range(cols):
            # Check diagonal top-left to bottom-right (↘)
            if row + target_len <= rows and col + target_len <= cols:
                if (matrix[row][col] == target[0] and 
                    matrix[row+1][col+1] == target[1] and
                    matrix[row+2][col+2] == target[2]):
                    # Store position of "A" (which is at row+1, col+1)
                    matches.append((row+1, col+1))

            # Check diagonal bottom-left to top-right (↗)
            if row - target_len + 1 >= 0 and col + target_len <= cols:
                if (matrix[row][col] == target[0] and 
                    matrix[row-1][col+1] == target[1] and
                    matrix[row-2][col+2] == target[2]):
                    # Store position of "A" (which is at row-1, col+1)
                    matches.append((row-1, col+1))

            # Check diagonal top-right to bottom-left (↙)
            if row + target_len <= rows and col - target_len + 1 >= 0:
                if (matrix[row][col] == target[0] and 
                    matrix[row+1][col-1] == target[1] and
                    matrix[row+2][col-2] == target[2]):
                    # Store position of "A" (which is at row+1, col-1)
                    matches.append((row+1, col-1))

            # Check diagonal bottom-right to top-left (↖)
            if row - target_len + 1 >= 0 and col - target_len + 1 >= 0:
                if (matrix[row][col] == target[0] and 
                    matrix[row-1][col-1] == target[1] and
                    matrix[row-2][col-2] == target[2]):
                    # Store position of "A" (which is at row-1, col-1)
                    matches.append((row-1, col-1))

    # Count how many times the same (row, col) of "A" appears in the matches
    position_count = {}
    for match in matches:
        if match not in position_count:
            position_count[match] = 0
        position_count[match] += 1

    # Return the number of positions that appeared more than once
    return sum(1 for count in position_count.values() if count > 1)

# Find the amount of repeated positions for "A"
repeated_positions = count_matching_mas(matrix, target)

# Output the results
print(f"Number of repeated positions for 'A' in matches: {repeated_positions}")
