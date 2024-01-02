def znajdź_indeksy_wystąpień(lista, szukana_liczba):
    indeksy = [i for i, x in enumerate(lista) if x == szukana_liczba]
    return indeksy

lista1 = [1, 2, 3, 4, 5, 2]
szukana_liczba1 = 2
print("Oryginalna lista liczb:", lista1)
print("Podana liczba", szukana_liczba1)
print("Indeksy wszystkich wystąpień danej liczby w liście:")
print(znajdź_indeksy_wystąpień(lista1, szukana_liczba1))

lista2 = [3, 1, 2, 3, 4, 5, 6, 3, 3]
szukana_liczba2 = 3
print("\nOryginalna lista liczb:", lista2)
print("Podana liczba", szukana_liczba2)
print("Indeksy wszystkich wystąpień danej liczby w liście:")
print(znajdź_indeksy_wystąpień(lista2, szukana_liczba2))

lista3 = [1, 2, 3, -4, 5, 2, -4]
szukana_liczba3 = -4
print("\nOryginalna lista liczb:", lista3)
print("Podana liczba", szukana_liczba3)
print("Indeksy wszystkich wystąpień danej liczby w liście:")
print(znajdź_indeksy_wystąpień(lista3, szukana_liczba3))

lista4 = [1, 2, 3, 4, 5, 2]
szukana_liczba4 = 7
print("\nOryginalna lista liczb:", lista4)
print("Podana liczba", szukana_liczba4)
print("Indeksy wszystkich wystąpień danej liczby w liście:")
print(znajdź_indeksy_wystąpień(lista4, szukana_liczba4))