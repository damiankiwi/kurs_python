def is_symmetrical(number):
    str_number = str(number)
    return str_number == str_number[::-1]

input1 = 121
output1 = is_symmetrical(input1)
print(output1)

input2 = 0
output2 = is_symmetrical(input2)
print(output2)

input3 = 122
output3 = is_symmetrical(input3)
print(output3)

input4 = 990099
output4 = is_symmetrical(input4)
print(output4)