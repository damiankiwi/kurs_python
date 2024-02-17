def filter_numbers(input_list):
    result = [num for num in input_list if num > 10 and int(str(num)[0]) % 2 != 0 and int(str(num)[-1]) % 2 != 0]
    return result

input1 = [1, 3, 79, 10, 4, 1, 39, 62]
output1 = filter_numbers(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = [11, 31, 77, 93, 48, 1, 57]
output2 = filter_numbers(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")