def reverse_case_and_string(lst):
    result = []
    for s in lst:
        if any(c.isalpha() for c in s):
            result.append(s.swapcase())
        else:
            result.append(s[::-1])
    return result

input1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
output1 = reverse_case_and_string(input1)
print(f"Original list:\n{input1}\nReverse the case of all strings. "
      f"For those strings which contain no letters, reverse the strings:\n{output1}")

input2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
output2 = reverse_case_and_string(input2)
print(f"\nOriginal list:\n{input2}\nReverse the case of all strings. "
      f"For those strings which contain no letters, reverse the strings:\n{output2}")

input3 = ['Hello', '!@#', '!@#$', '123#@!']
output3 = reverse_case_and_string(input3)
print(f"\nOriginal list:\n{input3}\nReverse the case of all strings. "
      f"For those strings which contain no letters, reverse the strings:\n{output3}")