array = [1, 2, 3, 5, 7, 8, 9, 10]

count_even_odd = lambda arr: (len([x for x in arr if x % 2 == 0]), len([x for x in arr if x % 2 != 0]))

even_count, odd_count = count_even_odd(array)

print("Number of even numbers in the above array:", even_count)
print("Number of odd numbers in the above array:", odd_count)