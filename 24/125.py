def consecutive_vowel_check(input_string):
    vowels = "aeiouAEIOU"
    words = input_string.split()

    for i in range(len(words) - 1):
        if words[i][-1] in vowels and words[i + 1][0] in vowels:
            return True

    return False

sample_data = [
    "These exercises can be used for practice.",
    "Following exercises should be removed for practice.",
    "I use these stories in my classroom."
]

for data in sample_data:
    print(f'"{data}" -> {consecutive_vowel_check(data)}')