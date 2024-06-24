import itertools

def generate_color_combinations(colors, n):
    return list(itertools.combinations_with_replacement(colors, n))

colors = ['Red', 'Green', 'Blue']
n = 2

combinations = generate_color_combinations(colors, n)
print(f"Unique combinations of {n} colors from {colors}:")
for combo in combinations:
    print(combo)

n = 3
combinations = generate_color_combinations(colors, n)
print(f"\nUnique combinations of {n} colors from {colors}:")
for combo in combinations:
    print(combo)