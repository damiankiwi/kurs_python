"""2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”."""


number1 = float(input("Podaj pierwszą liczbę ->"))
number2 = float(input("Podaj drugą liczbę ->"))

number3 = number1 + number2

if number3 >= 101:
    print(number3)
else:
    print("Koniec")