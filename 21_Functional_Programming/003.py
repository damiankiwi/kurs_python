def multiply_numbers(numbers):

    result = 1
    for num in numbers:
        result *= num
    return result

num_list = [8, 2, 3, -1, 7]
print("Product of numbers:", multiply_numbers(num_list))