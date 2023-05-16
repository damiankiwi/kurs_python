#2. Napisać funkcję, która sprawdza czy liczba jest parzysta.

user_number = int(input("Podaj liczbę do sprawdzenia: "))

def is_even(number):
    if number % 2 == 0:
        print('Podana liczba jest parzysta')
    else:
        print('Podana liczba nieparzysta')

is_even(user_number)