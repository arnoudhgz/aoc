from arg_utils import get_file_name

def find_fields(matrix):
    """Find and mark distinct fields in the matrix."""
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    fields = {}

    def dfs(row, col, patch_type, field_id):
        """Depth-first search to explore a field."""
        # Check bounds, visited status, and patch type
        if (row < 0 or row >= rows or col < 0 or col >= cols or
            visited[row][col] or matrix[row][col] != patch_type):
            return

        visited[row][col] = True
        fields[field_id].append((row, col))

        # Explore adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            dfs(row + dx, col + dy, patch_type, field_id)

    # Identify and label fields
    field_count = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                patch_type = matrix[i][j]
                field_id = (patch_type, field_count)
                fields[field_id] = []
                dfs(i, j, patch_type, field_id)
                field_count += 1

    return fields

def count_sides_and_patches(matrix):
    """Count sides and patches for each field."""
    fields = find_fields(matrix)
    side_counts = {}
    patch_counts = {}

    # Track the sides for each patch, ensuring all values are unique
    patch_sides = {}

    for field_id, locations in fields.items():
        patch_type = field_id[0]

        # Count patches (area of the region)
        patch_count = len(locations)
        patch_counts[field_id] = patch_count

        # Initialize patch sides count for each patch as a set (ensures uniqueness)
        patch_sides[field_id] = set()

        # Count all sides (potential external sides)
        for row, col in locations:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                side = (new_row, new_col)  # Define the side by its two endpoints

                # If the neighboring cell is out of bounds, it's an external side
                if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
                    patch_sides[field_id].add(side)
                # If the neighboring cell is a different patch type, count as external
                elif matrix[new_row][new_col] != patch_type:
                    patch_sides[field_id].add(side)

        # Store total external sides for the patch
        print(field_id, patch_sides[field_id], "\n")
        side_counts[field_id] = len(set(patch_sides[field_id]))

    return patch_counts, side_counts

# Use the utility function to get the file name
file_name = get_file_name(__file__)

# Read the grid
grid = []
with open(file_name, 'r') as file:
    for line in file:
        grid.append(line.strip())

matrix = [list(row) for row in grid]

# Find patches and count sides
patch_counts, side_counts = count_sides_and_patches(matrix)

# Define total_costs
total_costs = 0

# Print results
print("Fields, Patches, and Sides:")
for field_id, patches in patch_counts.items():
    sides = side_counts[field_id]
    costs = patches * sides
    total_costs += costs
    print(f"Field {field_id[1]} (Patch {field_id[0]}): {patches} patches, {sides} sides, costs: {costs}")

print("==============================")
print("Total costs: ", total_costs)
