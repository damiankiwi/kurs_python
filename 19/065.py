def shift_decimal(n, shift):
    num_str = str(n)
    length = len(num_str)

    if shift >= length:
        result = num_str[::-1]
    else:
        result = num_str[shift:] + num_str[:shift]

    return int(result)

n1, shift1 = 12345, 1
result1 = shift_decimal(n1, shift1)
print(f"Input:\n{n1}, Shift: {shift1}\nOutput:\nResult = {result1}")

n2, shift2 = 12345, 2
result2 = shift_decimal(n2, shift2)
print(f"\nInput:\n{n2}, Shift: {shift2}\nOutput:\nResult = {result2}")

n3, shift3 = 12345, 3
result3 = shift_decimal(n3, shift3)
print(f"\nInput:\n{n3}, Shift: {shift3}\nOutput:\nResult = {result3}")

n4, shift4 = 12345, 5
result4 = shift_decimal(n4, shift4)
print(f"\nInput:\n{n4}, Shift: {shift4}\nOutput:\nResult = {result4}")

n5, shift5 = 12345, 6
result5 = shift_decimal(n5, shift5)
print(f"\nInput:\n{n5}, Shift: {shift5}\nOutput:\nResult = {result5}")