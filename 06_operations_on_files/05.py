"""Moje"""
def get_file():
    with open('pan_tadzio.txt', encoding = 'utf-8') as fopen:
        content = fopen.read()

    return content

def find_longest_word(text):
    text = text.split()
    longest_word = ''

    for check_word in text:
        if len(check_word) > len(longest_word):
            longest_word = check_word

    return longest_word


text = get_file()
search_word = find_longest_word(text)

print("Najdłuższe słowo w pliku to:",search_word, ', o długości:', len(search_word))

# filename = "./intro/pan_tadzio.txt"
#
# with open(filename) as fopen:
#     content = fopen.read()
#
# content = content.replace(',', '').split()
#
# longest_word = ''
# for word in content:
#     if len(word) > len(longest_word):
#         print(word, '-', longest_word)
#         print(len(word),'-',  len(longest_word))
#         longest_word = word
#
# print("Najdłuże słowo to ... ", longest_word)