def compute_max_sum(diamond):
    n = len(diamond)

    for i in range(n - 2, -1, -1):
        for j in range(len(diamond[i])):
            if j + 1 < len(diamond[i + 1]):
                diamond[i][j] += max(diamond[i + 1][j], diamond[i + 1][j + 1])

    return diamond[0][0]

diamond_data = []
print("Podaj liczby (Ctrl+D aby zakończyć):")
try:
    for line in iter(input, ''):
        row = list(map(int, line.strip().split(',')))
        diamond_data.append(row)
except EOFError:
    pass

result = compute_max_sum(diamond_data)
print(f"Maksymalna wartość sumy przemieszczających się liczb: {result}")