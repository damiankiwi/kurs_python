import itertools


def shortest_distances(string, char):
    positions = [i for i, c in enumerate(string) if c == char]

    if not positions:
        return [float('inf')] * len(string)

    distances = []
    for i in range(len(string)):
        min_distance = min(abs(i - pos) for pos in positions)
        distances.append(min_distance)

    return distances


input_string = "loveleetcode"
specified_char = 'e'
print(f"Shortest distances to '{specified_char}' in '{input_string}':")
print(shortest_distances(input_string, specified_char))