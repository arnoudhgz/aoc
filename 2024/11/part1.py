from arg_utils import get_file_name

# Use the utility function to get the file name
file_name = get_file_name(__file__)

text = ""
with open(file_name, 'r') as file:
    for line in file:
        text += line

stones =  [int(item) for item in text.split()]

def blink(stones: enumerate) -> enumerate:
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue

        if len(str(stone)) % 2 == 0:
            stone_str = str(stone) 
            half_length = int(len(stone_str) / 2)

            new_stones.append(int(stone_str[:half_length]))
            new_stones.append(int(stone_str[half_length:]))
            continue

        new_stones.append(stone * 2024)

    return new_stones




for i in range(25):
    stones = blink(stones)

print(f"Amount of stones: {len(stones)}")