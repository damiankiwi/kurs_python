import random

random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 100))

numbers_less_than_50 = [num for num in random_numbers if num < 50]

print("Wylosowane liczby:")
print(random_numbers)
print("Liczby mniejsze niż 50:")
print(numbers_less_than_50)