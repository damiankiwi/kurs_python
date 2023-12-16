def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[n // 2]

    return median

input1 = [1, 2, 3, 4, 5]
output1 = calculate_median(input1)
print(output1)

input2 = [1, 2, 3, 4, 5, 6]
output2 = calculate_median(input2)
print(output2)

input3 = [6, 1, 2, 4, 5, 3]
output3 = calculate_median(input3)
print(output3)

input4 = [1.0, 2.11, 3.3, 4.2, 5.22, 6.55]
output4 = calculate_median(input4)
print(output4)

input5 = [1.0, 2.11, 3.3, 4.2, 5.22]
output5 = calculate_median(input5)
print(output5)

input6 = [2.0, 12.11, 22.3, 24.12, 55.22]
output6 = calculate_median(input6)
print(output6)