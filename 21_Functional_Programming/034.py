lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

filtered_values = list(filter(lambda x: len(x) == 6, lst))

print("Filtered values with length 6:")
for value in filtered_values:
    print(value)