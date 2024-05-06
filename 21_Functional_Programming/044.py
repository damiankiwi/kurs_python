def is_divisible_by_digits(num):
    for digit in str(num):
        if int(digit) == 0 or num % int(digit) != 0:
            return False
    return True

def find_numbers_in_range(start, end):
    result = [num for num in range(start, end + 1) if is_divisible_by_digits(num)]
    return result

start = 1
end = 25

result = find_numbers_in_range(start, end)

print(result)