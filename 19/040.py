def flip_case_and_replace_vowels(input_str):
    def replace_vowels(char):
        vowels = "aeiouAEIOU"
        if char in vowels:
            index = (vowels.index(char) + 2) % len(vowels)
            return vowels[index]
        return char

    flipped = input_str.swapcase()
    result = ''.join(replace_vowels(char) for char in flipped)
    return result

input1 = "Python"
output1 = flip_case_and_replace_vowels(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = "aeiou"
output2 = flip_case_and_replace_vowels(input2)
print(f"\nInput: {input2}\nOutput: {output2}")

input3 = "Hello, world!"
output3 = flip_case_and_replace_vowels(input3)
print(f"\nInput: {input3}\nOutput: {output3}")

input4 = "AEIOU"
output4 = flip_case_and_replace_vowels(input4)
print(f"\nInput: {input4}\nOutput: {output4}")