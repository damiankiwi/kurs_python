"""8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej."""

number1 = float(input("Podaj pierwszą liczbę ->"))
number2 = float(input("Podaj drugą liczbę ->"))
number3 = float(input("Podaj trzecią liczbę ->"))

numbers = (number1, number2, number3)

print(sorted(numbers))