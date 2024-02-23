def closest_pair_indices(numbers):
    min_distance = float('inf')
    closest_indices = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])

            if distance < min_distance:
                min_distance = distance
                closest_indices = [i, j]

    return closest_indices

input1 = [1, 7, 9, 2, 10]
output1 = closest_pair_indices(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = [1.1, 4.25, 0.79, 1.0, 4.23]
output2 = closest_pair_indices(input2)
print(f"\nInput: {input2}\nOutput: {output2}")

input3 = [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
output3 = closest_pair_indices(input3)
print(f"\nInput: {input3}\nOutput: {output3}")