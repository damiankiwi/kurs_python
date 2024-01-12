def czy_calowita_srednia(tablica):
    srednia = sum(tablica) / len(tablica)
    return srednia.is_integer()

array1 = [1, 3, 5, 7, 9]
print("Oryginalna tablica:", array1)
print("Sprawdź czy średnia wartość elementów tej tablicy jest liczbą całkowitą:", czy_calowita_srednia(array1))

array2 = [2, 4, 2, 6, 4, 8]
print("Oryginalna tablica:", array2)
print("Sprawdź czy średnia wartość elementów tej tablicy jest liczbą całkowitą:", czy_calowita_srednia(array2))