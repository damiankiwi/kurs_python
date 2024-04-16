def is_pangram(sentence):
    sentence = sentence.lower()

    letters = set(sentence)

    letters.discard(' ')
    letters.discard(',')
    letters.discard('.')

    return len(letters) == 26

sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")