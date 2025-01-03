def word_starts_and_ends_with_vowel(input_string):
    vowels = "aeiouAEIOU"
    words = input_string.split()

    for word in words:
        if len(word) > 1 and word[0] in vowels and word[-1] in vowels:
            return True

    return False

sample_data = [
    "Red Orange White",
    "Red White Black",
    "abcd dkise eosksu"
]

for data in sample_data:
    print(f'"{data}" -> {word_starts_and_ends_with_vowel(data)}')