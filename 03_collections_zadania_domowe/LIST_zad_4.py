# 4. Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

arr = []
num = int(input("Jaką ilość parzystych elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do list ->")
    arr.append(item)

print(arr)

if len(arr) % 2 == 0 and len(arr) > 0:
    if arr[int(len(arr)/2)] == arr[int(len(arr)/2) - 1]:

        print('Elementy są takie same')
    else:
        print('Elementy nie są takie same')
