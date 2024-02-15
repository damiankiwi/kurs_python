def find_and_sort_even_length_words(word_list):
    even_length_words = [word for word in word_list if len(word) % 2 == 0]
    sorted_even_length_words = sorted(even_length_words, key=len)
    return sorted_even_length_words

input1 = ['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
output1 = find_and_sort_even_length_words(input1)
print(f"Original list of words:\n{input1}\nFind the even-length words and sort them by length:\n{output1}")

input2 = ['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
output2 = find_and_sort_even_length_words(input2)
print(f"\nOriginal list of words:\n{input2}\nFind the even-length words and sort them by length:\n{output2}")