def print_matrix_in_order(matrix):
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            print(*row)
        else:
            print(*row[::-1])

input_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [0, 6, 2, 8],
    [2, 3, 0, 2]
]

print_matrix_in_order(input_matrix)