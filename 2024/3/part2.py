from arg_utils import get_file_name
import re

pattern = r'mul\((-?\d+),(-?\d+)\)'

# Use the utility function to get the file name
file_name = get_file_name(__file__)

text = ""
with open(file_name, 'r') as file:
    for line in file:
        text += line
        
parts = re.split(r"(don't\(\))|(do\(\))", text)

# Variable to track whether we are in "don't()" pause mode
paused = False

# Store the results
matches = []

# Process each part of the string
for part in parts:
    if part is None:
        continue
    if part == "don't()":
        paused = True
    elif part == "do()":
        paused = False
    elif not paused:
        # Find all matches for 'mul(<int>,<int>)' if not paused
        matches.extend(re.findall(pattern, part))

total = 0;        
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)