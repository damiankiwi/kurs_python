def sum_of_squares(num):
    return sum(int(digit) ** 2 for digit in str(num))

def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    return num == 1

def find_first_n_happy_numbers(n):
    happy_numbers = []
    num = 1
    while len(happy_numbers) < n:
        if is_happy_number(num):
            happy_numbers.append(num)
        num += 1
    return happy_numbers

n = 10
result = find_first_n_happy_numbers(n)
print(result)