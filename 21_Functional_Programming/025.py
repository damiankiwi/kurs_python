original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(original_list)

even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
print("Even numbers from the said list:")
print(even_numbers)

odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))
print("Odd numbers from the said list:")
print(odd_numbers)