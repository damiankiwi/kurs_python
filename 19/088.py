import random


def generate_number(even_digits, odd_digits):
    number = []

    number.append(str(random.randint(1, 9) * 2))

    for _ in range(even_digits - 1):
        number.append(str(random.randint(0, 4) * 2))

    for _ in range(odd_digits):
        number.append(str(random.randint(1, 4) * 2 - 1))

    random.shuffle(number)

    result = int(''.join(number))

    return result

even_digits = 2
odd_digits = 3
output1 = generate_number(even_digits, odd_digits)

even_digits = 4
odd_digits = 7
output2 = generate_number(even_digits, odd_digits)

print(f"Number of even digits: {even_digits}, Number of odd digits: {odd_digits}")
print(f"Output 1: {output1}")
print(f"Output 2: {output2}")