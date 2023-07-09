def liczba_wystapien_a(ciag):
    count = 0
    for znak in ciag:
        if znak == 'a':
            count += 1
    return count

ciag_znakow = input("Podaj ciąg znaków: ")
liczba_a = liczba_wystapien_a(ciag_znakow)
print(f"Liczba wystąpień litery 'a': {liczba_a}")