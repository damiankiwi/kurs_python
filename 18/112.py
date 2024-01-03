def digit_distance(num1, num2):
    num1_digits = [int(digit) for digit in str(num1)]
    num2_digits = [int(digit) for digit in str(num2)]

    len_diff = abs(len(num1_digits) - len(num2_digits))
    if len(num1_digits) < len(num2_digits):
        num1_digits = [0] * len_diff + num1_digits
    else:
        num2_digits = [0] * len_diff + num2_digits

    distance = sum(abs(d1 - d2) for d1, d2 in zip(num1_digits, num2_digits))

    return distance

print(digit_distance(123, 256))
print(digit_distance(23, 56))
print(digit_distance(1, 2))
print(digit_distance(24232, 45645))