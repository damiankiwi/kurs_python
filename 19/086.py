def find_vowels(texts):
    vowels = set("aeiouyAEIOUY")
    result = []

    for text in texts:
        current_vowels = ""
        current_word = ""

        for char in text:
            if char.isalpha():
                current_word += char
            else:
                if current_word:
                    current_vowels += current_word[-1] if current_word[-1] in vowels else ""
                    current_word = ""

        current_vowels += current_word[-1] if current_word[-1] in vowels else ""
        result.append(current_vowels)

    return result

input1 = ['w3resource', 'Python', 'Java', 'C++']
output1 = find_vowels(input1)

input2 = ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
output2 = find_vowels(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")