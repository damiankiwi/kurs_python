def find_closest_numbers(numbers):
    numbers.sort()
    min_difference = float('inf')
    closest_pair = []

    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]

        if difference < min_difference and numbers[i] != numbers[i + 1]:
            min_difference = difference
            closest_pair = [numbers[i], numbers[i + 1]]

    return closest_pair

input1 = [1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
output1 = find_closest_numbers(input1)

input2 = [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
output2 = find_closest_numbers(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")