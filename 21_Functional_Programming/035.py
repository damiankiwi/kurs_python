"15"
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, list1, list2))

print("Result after adding two lists:")
print(result)