def uppercase_vowels_positions(s):
    vowels = "AEIOU"
    return [i for i, char in enumerate(s[1::2]) if char in vowels]

input1 = "w3rEsOUrcE"
output1 = uppercase_vowels_positions(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = "AEIOUYW"
output2 = uppercase_vowels_positions(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")