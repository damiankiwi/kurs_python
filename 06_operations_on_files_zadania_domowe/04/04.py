import random
def get_content():
    filename = "quotes.txt"
    # filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
    with open(filename) as fopen:
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
    for i in range(3):
        quotes = get_content()
        quote = random.choice(quotes)
        show(quote)


if __name__ == '__main__':
    main()