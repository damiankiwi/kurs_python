def create_string_with_counts(char_counts):
    result = []

    for char, count in char_counts.items():
        result.extend([char] * count)

    return ' '.join(result)

input1 = {'f': 1, 'o': 2}
output1 = create_string_with_counts(input1)

input2 = {'a': 1, 'b': 1, 'c': 1}
output2 = create_string_with_counts(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")