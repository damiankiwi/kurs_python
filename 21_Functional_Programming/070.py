original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
words_to_remove = ['orange', 'black']

remove_words = lambda lst, words: list(filter(lambda x: x not in words, lst))

filtered_list = remove_words(original_list, words_to_remove)

print("Original list:")
print(original_list)
print("Remove words:")
print(words_to_remove)
print("After removing the specified words from the said list:")
print(filtered_list)