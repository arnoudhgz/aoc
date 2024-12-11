import time
from collections import defaultdict
from arg_utils import get_file_name

def blink(stones_count):
    # Use defaultdict for more efficient counting
    new_stones_count = defaultdict(int)

    for stone, count in stones_count.items():
        if stone == 0:
            new_stones_count[1] += count
        else:
            # Convert to string only once and use integer operations
            stone_str = str(stone)
            str_len = len(stone_str)
            
            if str_len % 2 == 0:
                # Avoid repeated string conversions and slicing
                half_length = str_len // 2
                first_half = int(stone_str[:half_length])
                second_half = int(stone_str[half_length:])
                new_stones_count[first_half] += count
                new_stones_count[second_half] += count
            else:
                # Avoid repeated multiplication
                new_stones_count[stone * 2024] += count

    return new_stones_count

def process_stones(stones, iterations=1):
    # Convert input to counter more efficiently
    stones_count = defaultdict(int)
    for stone in stones:
        stones_count[stone] += 1

    # Use in-place iteration to reduce memory overhead
    for _ in range(iterations):
        stones_count = blink(stones_count)

    return stones_count

def main():
    # Use the utility function to get the file name
    file_name = get_file_name(__file__)

    text = ""
    with open(file_name, 'r') as file:
        for line in file:
            text += line

    stones =  [int(item) for item in text.split()]

    iteration_count = 75

    # Capture start time with high-resolution timer
    start_time = time.perf_counter()

    # Process the stones
    stones_count = process_stones(stones, iterations=iteration_count)

    # Capture end time
    end_time = time.perf_counter()

    # Final result after the last iteration
    final_stones_count = sum(stones_count.values())
    
    # Calculate and print the time taken in milliseconds
    execution_time_ms = (end_time - start_time) * 1000
    
    print(f"Final amount of stones: {final_stones_count}")
    print(f"Execution time: {execution_time_ms:.2f} ms")

if __name__ == "__main__":
    main()