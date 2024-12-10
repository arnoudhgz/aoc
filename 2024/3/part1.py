from arg_utils import get_file_name
import re

pattern = r'mul\((-?\d+),(-?\d+)\)'

# Use the utility function to get the file name
file_name = get_file_name(__file__)

text = ""
with open(file_name, 'r') as file:
    for line in file:
        text += line
        
matches = re.findall(pattern, text)

total = 0;        
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)