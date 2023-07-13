suma = 0
for liczba in range(1, 101):
    if liczba % 2 == 0:
        suma += liczba
        if liczba % 3 == 0:
            print(str(liczba) + "!", end=" ")
        else:
            print(str(liczba), end=" ")

print("\nSuma liczb parzystych: " + str(suma))