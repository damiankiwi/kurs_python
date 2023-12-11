def is_palindrome(number):
    if number < 0:
        return False

    str_number = str(number)
    return str_number == str_number[::-1]

input1 = 100
output1 = is_palindrome(input1)
print(output1)

input2 = 252
output2 = is_palindrome(input2)
print(output2)

input3 = -838
output3 = is_palindrome(input3)
print(output3)