def find_substring_with_vowel(input_str):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = ""

    for i in range(len(input_str) - 2):
        if input_str[i] in consonants and input_str[i + 1] in vowels and input_str[i + 2] in consonants:
            result = input_str[i:i+3]
            break

    return result

input1 = "Hello"
output1 = find_substring_with_vowel(input1)

input2 = "Sandwich"
output2 = find_substring_with_vowel(input2)

input3 = "Python"
output3 = find_substring_with_vowel(input3)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")

print(f"Input 3: {input3}")
print(f"Output 3: {output3}")