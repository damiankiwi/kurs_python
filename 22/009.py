import itertools

def split_iterable(iterable, n):
    return itertools.tee(iterable, n)

data = [1, 2, 3, 4, 5]

split_data = split_iterable(data, 3)

for i, it in enumerate(split_data):
    print(f'Iterator {i+1}: {list(it)}')