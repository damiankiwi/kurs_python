"""moje"""
# import random
#
# def get_content():
#     with open('quotes.txt') as fopen:
#         content = fopen.readlines()
#
#     return content
#
#
# def show(quote):
#
#     quote = quote.split(' - ')
#
#     print('Quote of the day is:')
#     print()
#     width = 60
#     print('*' * width)
#     print(quote[0].strip().center(width))
#     print(quote[1].strip().center(width))
#     print('*' * width)
#
#
# def main():
#     quotes = get_content()
#     quote = random.choice(quotes)
#     show(quote)
#
# main()

import random
def get_content():
    filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
    with open(f'{filename}.txt') as fopen:
        content = fopen.readlines()

    return content


def show(quote):
    txt, author = quote.split(' - ')
    print('Quote of the day is:')
    print()
    width = 70
    print('*' * width)
    print(txt.center(width))
    print(author.strip().center(width))
    print('*' * width)


def main():
    quotes = get_content()
    quote = random.choice(quotes)
    show(quote)

main()