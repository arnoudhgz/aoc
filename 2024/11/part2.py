import time
from collections import Counter

# Sample input
stones = [1950139, 0, 3, 837, 6116, 18472, 228700, 45]

# Define the blink function using a dictionary to store counts
def blink(stones_count):
    new_stones_count = Counter()

    for stone, count in stones_count.items():
        if stone == 0:
            new_stones_count[1] += count  # If the stone is 0, it turns into 1
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                # Split the stone into two parts if it has an even number of digits
                half_length = len(stone_str) // 2
                first_half = int(stone_str[:half_length])
                second_half = int(stone_str[half_length:])
                new_stones_count[first_half] += count
                new_stones_count[second_half] += count
            else:
                new_stones_count[stone * 2024] += count  # For odd-length stones, multiply by 2024

    return new_stones_count

# Process the stones in-place and perform iterations
def process_stones(stones_count, iterations=1):
    for _ in range(iterations):
        stones_count = blink(stones_count)  # Update the dictionary of stone counts
    return stones_count

# Convert the initial list of stones to a Counter (frequency dictionary)
stones_count = Counter(stones)

# Perform processing incrementally, 1 iteration at a time
iteration_count = 75  # Track iteration count

# Capture start time
start_time = time.time()

# Process the stones one iteration at a time
stones_count = process_stones(stones_count, iterations=iteration_count)

# Capture end time
end_time = time.time()

# Final result after the last iteration
final_stones_count = sum(stones_count.values())  # Total number of stones after all iterations
print(f"Final amount of stones: {final_stones_count}")

# Calculate and print the time taken in milliseconds
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} ms")
