import itertools

def infinite_cycle(iterable):
    return itertools.cycle(iterable)

input_list = ['A', 'B', 'C']

iterator = infinite_cycle(input_list)

print("First 10 values from the infinite cycle iterator:")
for _ in range(10):
    print(next(iterator))