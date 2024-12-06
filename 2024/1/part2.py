from arg_utils import get_file_name
from collections import Counter

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

# Count occurrences of each value in array2
counter = Counter(column2)

# Calculate the sum
result = sum(value * counter[value] for value in column1)

print(f"The result is: {result}")