#Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna
#przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

"""num = int(input("Podaj liczbe: "))
if num % 3 == 0 :
    print("Twoja liczba jest podzielna przez 3")
else:
    print("Twoja liczba nie jest podzielna przez 3")"""


number = float(input("Podaj liczbę ->"))

if number % 3 == 0:
    print("Podzielna przez 3")
else:
    print("Nie podzielna przez 3")
