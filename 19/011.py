def indeksy_ponizej_progu(lista, prog):
    indeksy = [i for i, num in enumerate(lista) if num < prog]
    return indeksy

lista1 = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
prog1 = 100
print("Original list:")
print(lista1)
print(f"Threshold: {prog1}")
print("Check the indexes of numbers of the said list below the given threshold:")
print(indeksy_ponizej_progu(lista1, prog1))

lista2 = [0, 12, 4, 3, 49, 9, 1, 5, 3]
prog2 = 10
print("\nOriginal list:")
print(lista2)
print(f"Threshold: {prog2}")
print("Check the indexes of numbers of the said list below the given threshold:")
print(indeksy_ponizej_progu(lista2, prog2))