def minimalize_mean_squared_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    best_x = min(numbers, key=lambda x: sum((num - x)**2 for num in numbers))
    return best_x

input1 = [4, -5, 17, -9, 14, 108, -9]
output1 = minimalize_mean_squared_deviation(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [12, -2, 14, 3, -15, 10, -45, 3, 30]
output2 = minimalize_mean_squared_deviation(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")