def round_and_square(numbers):
    running_total = 0
    result = []

    for num in numbers:
        rounded_num = int(num + 0.5)
        running_total += rounded_num**2
        result.append(running_total)

    return result

input1 = [2.6, 3.5, 6.7, 2.3, 5.6]
output1 = round_and_square(input1)

input2 = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
output2 = round_and_square(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")