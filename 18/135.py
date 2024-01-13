import math

def najmniejsza_wspolna_wielokrotnosc(lista):
    result = 1
    for number in lista:
        result = result * number // math.gcd(result, number)
    return result

arr1 = [4, 6, 8]
print("Oryginalne elementy listy:", arr1)
print("Najmniejsza wspólna wielokrotność liczb z tej listy:", najmniejsza_wspolna_wielokrotnosc(arr1))

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Oryginalne elementy listy:", arr2)
print("Najmniejsza wspólna wielokrotność liczb z tej listy:", najmniejsza_wspolna_wielokrotnosc(arr2))

arr3 = [48, 72, 108]
print("Oryginalne elementy listy:", arr3)
print("Najmniejsza wspólna wielokrotność liczb z tej listy:", najmniejsza_wspolna_wielokrotnosc(arr3))