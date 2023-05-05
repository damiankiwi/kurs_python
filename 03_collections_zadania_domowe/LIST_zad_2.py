# 2. Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

list_num = []

for i in range(10):
    my_numbers = input('Podaj 10 liczb: ')
    list_num.append(my_numbers)

print('Liczby niepparzyste:')

for number in list_num:
    if int(number) % 2 != 0:
        print(number, end=', ')
