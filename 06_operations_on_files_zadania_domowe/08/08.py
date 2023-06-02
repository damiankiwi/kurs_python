import random


def get_file():
    with open('dane.csv', encoding='utf-8') as f:
        content = f.readlines()
    return content


first = []
second = []


def main():
    content = get_file()
    for line in content:
        splitted_line = line.split(';')
        first.append(splitted_line[0])
        second.append(splitted_line[1])

    part_one = random.choice(first)
    part_two = random.choice(second)
    print("Generator tytułu konferencji naukowej:\n")
    print(f'{part_one} {part_two}')


if __name__ == '__main__':
    main()
