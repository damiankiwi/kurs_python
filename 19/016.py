def find_strings_with_substring(substring, string_list):
    result = [word for word in string_list if substring in word]
    return result

input1 = ('ca', ['cat', 'car', 'fear', 'center'])
output1 = find_strings_with_substring(*input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = ('o', ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''])
output2 = find_strings_with_substring(*input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")

input3 = ('oe', ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''])
output3 = find_strings_with_substring(*input3)
print(f"\nInput:\n{input3}\nOutput:\n{output3}")