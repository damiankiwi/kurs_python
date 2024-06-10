import itertools

data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('a', 5), ('c', 6)]

def group_by_key(iterable):
    return itertools.groupby(iterable, key=lambda x: x[0])

grouped_data = group_by_key(data)

for key, group in grouped_data:
    print(f'Key: {key}')
    print(f'Group: {list(group)}')