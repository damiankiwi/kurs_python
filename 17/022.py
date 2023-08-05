def licz_wystapienia_liczby_4(lista):
    licznik = 0
    for element in lista:
        if element == 4:
            licznik += 1
    return licznik

dana_lista = [1, 4, 2, 4, 5, 4, 8, 9, 4]
wynik = licz_wystapienia_liczby_4(dana_lista)
print(f"Liczba wystąpień liczby 4 w liście: {wynik}")