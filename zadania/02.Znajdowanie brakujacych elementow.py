def brakujace_elementy(lista, n):
    wynik = []
    for i in range(1, n + 1):
        if i not in lista:
            wynik.append(i)
    return wynik

print(brakujace_elementy([2, 3, 7, 4, 9], 10))