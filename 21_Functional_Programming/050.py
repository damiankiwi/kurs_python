def sort_matrix_by_row_sum(matrix):
    sorted_matrix = sorted(matrix, key=lambda x: sum(x))
    return sorted_matrix

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

print("Original Matrix:")
print(matrix1)
print("Sort the said matrix in ascending order according to the sum of its rows:")
print(sort_matrix_by_row_sum(matrix1))

print("\nOriginal Matrix:")
print(matrix2)
print("Sort the said matrix in ascending order according to the sum of its rows:")
print(sort_matrix_by_row_sum(matrix2))