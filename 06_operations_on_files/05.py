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