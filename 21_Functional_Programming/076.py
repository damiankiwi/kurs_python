base_list = [2, 3, 4, 5]

power_list = list(map(lambda x: x[1] ** x[0], enumerate(base_list)))

print("Original base list:")
print(base_list)
print("List containing the power of each base raised to the corresponding index:")
print(power_list)