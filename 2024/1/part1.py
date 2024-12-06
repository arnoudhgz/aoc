from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

# Now, let's read the selected file
column1 = []
column2 = []

with open(file_name, 'r') as file:
    for line in file:
        value1, value2 = line.split()
        column1.append(int(value1))
        column2.append(int(value2))

# Sort each column independently
column1_sorted = sorted(column1)
column2_sorted = sorted(column2)

# Initialize a list to store the distances
distances = []

# Loop through both sorted arrays and calculate the distance (absolute difference)
for val1, val2 in zip(column1_sorted, column2_sorted):
    distance = abs(val1 - val2)  # Calculate the absolute difference
    distances.append(distance)

# Sum the distances
total_distance = sum(distances)

# Print the distance sum
print("Total Sum of Distances:", total_distance)
