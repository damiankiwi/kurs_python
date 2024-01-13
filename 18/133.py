def najwieksza_suma(arr):
    suma_pozytywnych = sum(x for x in arr if x > 0)
    suma_negatywnych = sum(x for x in arr if x < 0)

    return max(suma_pozytywnych, suma_negatywnych)

arr1 = {0, 15, 16, 17, -14, -13, -12, -11, -10, 18, 19, 20}
print("Oryginalne elementy tablicy:", arr1)
print("Największa suma - Liczby dodatnie/ujemne tej tablicy:", najwieksza_suma(arr1))

arr2 = {0, 3, 4, 5, 9, -22, -44, -11}
print("Oryginalne elementy tablicy:", arr2)
print("Największa suma - Liczby dodatnie/ujemne tej tablicy:", najwieksza_suma(arr2))