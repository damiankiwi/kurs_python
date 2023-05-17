# 4. Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika
# zakresie. Powinna zwrócić komunikat:
# “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

number_a = int(input("podaj zakres od: "))
number_b = int(input("podaj zakres do: "))
number_c = int(input("podaj liczbę aby sprawdzić czy liczba znajduje się w zakresie: "))


def range_check():
    if number_b >= number_c >= number_a:
        print(f"Tak, liczba {number_c} znajduje się w zadanym zakresie")
    else:
        print(f"nie, liczba {number_c} jest z poza zakresu od {number_a} do {number_b}")


range_check()
