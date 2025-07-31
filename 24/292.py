from collections import Counter

text = "Python Exercise!"
letter_counter = Counter(text)

print("Letter Counter:")
for letter, count in letter_counter.items():
    if letter.isalpha():
        print(f"{letter}: {count}")