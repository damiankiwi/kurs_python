def sum_even_odd_indices(numbers):
    result = sum(numbers[i] for i in range(1, len(numbers), 2) if numbers[i] % 2 == 0)
    return result

input1 = [1, 2, 3, 4, 5, 6, 7]
output1 = sum_even_odd_indices(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [1, 2, 8, 3, 9, 4]
output2 = sum_even_odd_indices(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")