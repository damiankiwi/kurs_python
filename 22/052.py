words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

long_words = list(filter(lambda word: len(word) > 5, words))

print("Words with more than five letters:")
print(long_words)