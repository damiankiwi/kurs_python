def find_number_to_make_total_zero(numbers):
    total = sum(numbers)
    return -total

input1 = [1, 2, 3, 4, 5]
output1 = find_number_to_make_total_zero(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [-1, -2, -3, -4, 5]
output2 = find_number_to_make_total_zero(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")

input3 = [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
output3 = find_number_to_make_total_zero(input3)
print(f"\nInput:\n{input3}\nOutput:\n{output3}")