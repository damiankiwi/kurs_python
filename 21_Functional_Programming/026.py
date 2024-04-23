original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(original_list)

square_result = list(map(lambda x: x ** 2, original_list))
print("Square every number of the said list:")
print(square_result)

cube_result = list(map(lambda x: x ** 3, original_list))
print("Cube every number of the said list:")
print(cube_result)