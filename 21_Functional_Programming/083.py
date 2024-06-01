def compute_sum(array):
    integers = map(int, array)
    return sum(integers)

array_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total_sum = compute_sum(array_of_integers)

print("Array of integers:")
print(array_of_integers)
print("Sum of elements in the array:")
print(total_sum)