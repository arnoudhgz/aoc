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

        # Explore adjacent cells
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

def count_fences_and_patches(matrix):
    """Count fences and patches for each field."""
    fields = find_fields(matrix)
    fence_counts = {}
    patch_counts = {}

    for field_id, locations in fields.items():
        patch_type = field_id[0]
        
        # Count patches
        patch_counts[field_id] = len(locations)
        
        # Initialize fence tracking
        field_fences = 0
        field_patches = set(locations)
        
        # Check each patch in the field for surrounding fences
        for row, col in locations:
            # Check vertical fences
            if (row == 0) or (row > 0 and matrix[row-1][col] != patch_type):
                field_fences += 1  # Top fence
            if (row == len(matrix)-1) or (row < len(matrix)-1 and matrix[row+1][col] != patch_type):
                field_fences += 1  # Bottom fence
            
            # Check horizontal fences
            if (col == 0) or (col > 0 and matrix[row][col-1] != patch_type):
                field_fences += 1  # Left fence
            if (col == len(matrix[0])-1) or (col < len(matrix[0])-1 and matrix[row][col+1] != patch_type):
                field_fences += 1  # Right fence
        
        fence_counts[field_id] = field_fences

    return patch_counts, fence_counts

# Use the utility function to get the file name
file_name = get_file_name(__file__)

# Read the grid
grid = []
with open(file_name, 'r') as file:
    for line in file:
        grid.append(line.strip())

matrix = [list(row) for row in grid]

# Find patches and count fences
patch_counts, fence_counts = count_fences_and_patches(matrix)

# Define total_costs
total_costs = 0

# Print results
print("Fields, Patches, and Fences:")
for field_id, patches in patch_counts.items():
    fences = fence_counts[field_id]
    costs = patches * fences
    total_costs += costs
    print(f"Field {field_id[1]} (Patch {field_id[0]}): {patches} patches, {fences} fences, costs: {costs}")

print("==============================")
print("Total costs: ", total_costs)