from arg_utils import get_file_name
from typeguard import typechecked

# Use the utility function to get the file name
file_name = get_file_name(__file__)

@typechecked
def is_valid(value: int, previous_value: int) -> bool:
    if previous_value == -1:
        return True

    distance = abs(value - previous_value);

    return distance > 0 and distance < 4



line_count = 0  # Initialize a counter

with open(file_name, 'r') as file:
    for line in file:
        line_count += 1

        values = line.split()
        previous_value = -1
        increasing = False
        decreasing = False

        # Loop through values
        for value in values:
            new_value = int(value)

            if previous_value != -1:
                increasing = increasing or new_value > previous_value
                decreasing = decreasing or new_value < previous_value

            if increasing and decreasing:
                line_count -= 1
                break

            if not is_valid(new_value, previous_value):
                line_count -= 1
                break

            previous_value = new_value

print("Amount of safe lines:", line_count)