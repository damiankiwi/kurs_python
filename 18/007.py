with open('007.txt', 'r') as plik:
    tekst = plik.read()

czestotliwosc_znakow = {}

for znak in tekst:
    if znak in czestotliwosc_znakow:
        czestotliwosc_znakow[znak] += 1
    else:
        czestotliwosc_znakow[znak] = 1

for znak, liczba in czestotliwosc_znakow.items():
    if znak == '\n':
        print(f"Nowa linia: {liczba} wystąpień")
    elif znak == ' ':
        print(f'Spacja: {liczba} wystąpień')
    else:
        print(f"'{znak}': {liczba} wystąpień")