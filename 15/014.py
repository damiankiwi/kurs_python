def liczba_wystapien_e(tekst):
    liczba_e = 0
    indeks = 0

    while indeks < len(tekst):
        if tekst[indeks] == 'e' or tekst[indeks] == 'E':
            liczba_e += 1
        indeks += 1

    return liczba_e

ciag_znakow = input("Podaj ciąg znaków: ")

wynik = liczba_wystapien_e(ciag_znakow)
print("Liczba wystąpień litery 'e':", wynik)