from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

grid = []
with open(file_name, 'r') as file:
    for line in file:
        grid.append(line.replace("\n", ""))

# Create a matrix with all values converted to integers
matrix = [[int(value) for value in row] for row in grid]

def find_positions(arr, value):
    return [index for index, element in enumerate(arr) if element == value]

rowPositions = [];
for index, value in enumerate(matrix):
   # find all positions for 0
   result = find_positions(value, 0);
   if len(result) > 0:
      rowPositions.append((index, result))

# check for the next or previous column or next row if we can go to number 1 (and so on)
keepPositions = [];
for key, positions in rowPositions:
    for position in positions:
        try:
            if int(matrix[key][position]+1) == 1:
                keepPositions.append((key, int(matrix[key][position]+1)))

            if int(matrix[key][position]-1) == 1:
                keepPositions.append((key, int(matrix[key][position]-1)))

            if int(matrix[key+1][position]) == 1:
                keepPositions.append((key, int(matrix[key+1][position])))

            if int(matrix[key-1][position]) == 1:
                keepPositions.append((key, int(matrix[key-1][position])))
        except IndexError:
            continue



print(keepPositions)