from sympy import symbols, Eq, solve
from arg_utils import get_file_name

# Read the input file
file_name = get_file_name(__file__)
with open(file_name, 'r') as file:
    lines = [line.strip() for line in file if line.strip()]  # Skip blank lines

# Initialize results
results = []

# Process each group of 3 lines
for i in range(0, len(lines), 3):
    if i + 2 >= len(lines):  # Ensure there are enough lines
        print(f"Skipping incomplete set at index {i}")
        continue

    try:
        # Parse button A
        button_a = lines[i].split(":")[1].strip()
        ax, ay = map(int, button_a.replace("X+", "").replace("Y+", "").split(", "))

        # Parse button B
        button_b = lines[i + 1].split(":")[1].strip()
        bx, by = map(int, button_b.replace("X+", "").replace("Y+", "").split(", "))

        # Parse prize
        prize = lines[i + 2].split(":")[1].strip()
        px, py = map(int, prize.replace("X=", "").replace("Y=", "").split(", "))

        px = px + 10000000000000
        py = py + 10000000000000

        # Solve equations
        x, y = symbols('x y', integer=True)
        eq1 = Eq(ax * x + bx * y, px)  # X-axis equation
        eq2 = Eq(ay * x + by * y, py)  # Y-axis equation
        solution = solve((eq1, eq2), (x, y))

        # Check if solution is a list or dictionary
        if isinstance(solution, list) and solution:
            solution = solution[0]  # Take the first solution if multiple

        # Extract results
        hits_a = solution[x]
        hits_b = solution[y]
        total_cost = 3 * hits_a + 1 * hits_b  # Adjust costs as needed
        results.append((hits_a, hits_b, total_cost))
    except (IndexError, ValueError, KeyError, TypeError) as e:
        continue
    
total_costs = 0

# Print results
for idx, (hits_a, hits_b, total_cost) in enumerate(results, 1):
    total_costs += total_cost
    print(f"Set {idx}: Hits A={hits_a}, Hits B={hits_b}, Total Cost={total_cost}")

print("===================================")
print("Total costs: ", total_costs)