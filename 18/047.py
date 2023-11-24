text = input("Podaj tekst (tylko litery alfabetyczne i spacje): ")

words = text.split()

word_count = {}
word_length = {}

for word in words:
    word = ''.join(filter(str.isalpha, word))

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

    word_length[word] = len(word)

most_common_word = max(word_count, key=word_count.get)

longest_word = max(word_length, key=word_length.get)

print("Słowo występujące najczęściej:", most_common_word)
print("Słowo o największej liczbie liter:", longest_word)