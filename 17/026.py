def tworz_histogram(lista):
    histogram = {}
    for liczba in lista:
        if liczba in histogram:
            histogram[liczba] += 1
        else:
            histogram[liczba] = 1
    return histogram

dana_lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

histogram_wynik = tworz_histogram(dana_lista)

print("Histogram:")
for liczba, ilosc in histogram_wynik.items():
    print(f"{liczba}: {'*' * ilosc}")