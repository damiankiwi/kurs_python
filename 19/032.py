def rescale_and_shift(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return [(num - min_val) / range_val for num in numbers]

input1 = [18.5, 17.0, 18.0, 19.0, 18.0]
output1 = rescale_and_shift(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [13.0, 17.0, 17.0, 15.5, 2.94]
output2 = rescale_and_shift(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")