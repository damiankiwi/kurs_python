from collections import Counter

word = "Python Exercises"
vowels = "aeiouAEIOU"

vowel_ctr = Counter(c for c in word if c in vowels)

print("Vowel Counts:")
for vowel, count in vowel_ctr.items():
    print(f"{vowel}: {count}")