import itertools

def generate_combinations(colors, combination_length):
    return list(itertools.combinations_with_replacement(colors, combination_length))

colors = ['red', 'green', 'blue']
combination_length = 2

combinations = generate_combinations(colors, combination_length)

print('Combinations with repetitions:')
for combo in combinations:
    print(combo)