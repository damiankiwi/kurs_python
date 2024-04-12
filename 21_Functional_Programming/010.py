def print_even_numbers(numbers):

    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(numbers)