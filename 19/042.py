def distinct_characters_ignore_case(input_str):
    distinct_chars = list(set(input_str.lower()))
    distinct_chars.sort()
    return distinct_chars

input1 = "HELLO"
output1 = distinct_characters_ignore_case(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = "HelLo"
output2 = distinct_characters_ignore_case(input2)
print(f"\nInput: {input2}\nOutput: {output2}")

input3 = "Ignoring case"
output3 = distinct_characters_ignore_case(input3)
print(f"\nInput: {input3}\nOutput: {output3}")