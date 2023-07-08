array = input("Wprowadź elementy tablicy, oddzielając je przecinkami: ").split(",")
array = [int(x) for x in array]

index1 = int(input("Wprowadź indeks pierwszego elementu do zamiany: "))
index2 = int(input("Wprowadź indeks drugiego elementu do zamiany: "))

if index1 < 0 or index1 >= len(array) or index2 < 0 or index2 >= len(array):
    print("Niepoprawne indeksy.")
else:

    array[index1], array[index2] = array[index2], array[index1]
    print("Tablica po zamianie miejscami elementów:", array)
