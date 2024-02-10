def sort_numbers_based_on_strings(input_str):
    words = input_str.split()
    sorted_numbers = sorted(words, key=lambda x: int(x) if x.isdigit() else float('inf'))
    return ' '.join(sorted_numbers)

input1 = "six one four one two three"
output1 = sort_numbers_based_on_strings(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = "six one four three two nine eight"
output2 = sort_numbers_based_on_strings(input2)
print(f"\nInput: {input2}\nOutput: {output2}")

input3 = "nine eight seven six five four three two one"
output3 = sort_numbers_based_on_strings(input3)
print(f"\nInput: {input3}\nOutput: {output3}")