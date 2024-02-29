def find_numbers(numbers):
    negatives = [num for num in numbers if num < 0]
    positives = [num for num in numbers if num > 0]

    largest_negative = max(negatives, default=0)
    smallest_positive = min(positives, default=0)

    return [largest_negative, smallest_positive]

input1 = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
output1 = find_numbers(input1)

input2 = [-1, -2, -3, -4]
output2 = find_numbers(input2)

input3 = [1, 2, 3, 4]
output3 = find_numbers(input3)

input4 = []
output4 = find_numbers(input4)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")

print(f"Input 4: {input4}")
print(f"Output 4: {output4}")