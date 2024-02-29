def average_in_binary(a, b):
    numbers = list(range(a, b))

    if not numbers:
        return -1

    average = round(sum(numbers) / len(numbers))
    binary_average = bin(average)

    return binary_average

input1 = (4, 7)
output1 = average_in_binary(*input1)

input2 = (11, 19)
output2 = average_in_binary(*input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")