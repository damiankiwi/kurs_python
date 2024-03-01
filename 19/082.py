def has_only_odd_digits(num):
    odd_digits = set('13579')
    return all(digit in odd_digits for digit in str(abs(num)))

def odd_digits_sublist(lst):
    odd_digits_numbers = [num for num in lst if has_only_odd_digits(num)]
    return sorted(odd_digits_numbers)

input1 = [1, 3, 79, 10, 4, 2, 39]
output1 = odd_digits_sublist(input1)

input2 = [11, 31, 40, 68, 77, 93, 48, 1, 57]
output2 = odd_digits_sublist(input2)

input3 = [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
output3 = odd_digits_sublist(input3)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")