def find_string_with_most_unique_characters(strings):
    def count_unique_characters(s):
        return len(set(s))

    return max(strings, key=count_unique_characters)

input1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
output1 = find_string_with_most_unique_characters(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
output2 = find_string_with_most_unique_characters(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")