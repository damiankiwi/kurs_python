def inject_separator(numbers, separator):
    result = [numbers[0]]

    for num in numbers[1:]:
        result.extend([separator, num])

    return result

input1 = [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
separator1 = 6
output1 = inject_separator(input1, separator1)

input2 = [1, 2, 3, 4, 5, 6]
separator2 = 9
output2 = inject_separator(input2, separator2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")