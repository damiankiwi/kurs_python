original_list = [2, 4, 6, 9, 11]

given_number = 2

result = map(lambda x: x * given_number, original_list)

print("Result:")
print(*result)