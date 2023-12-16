import random

def generate_even_numbers(start, end, count):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return random.sample(even_numbers, count)

input_range = (1, 100)
output = generate_even_numbers(*input_range, count=10)
print(output)