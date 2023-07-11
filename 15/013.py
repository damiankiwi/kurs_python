import random

wylosowana_liczba = random.randint(1, 100)
zgadywana_liczba = None

while zgadywana_liczba != wylosowana_liczba:
    zgadywana_liczba = int(input("Podaj liczbę od 1 do 100: "))

    if zgadywana_liczba > wylosowana_liczba:
        print("Za duża liczba!")
    elif zgadywana_liczba < wylosowana_liczba:
        print("Za mała liczba!")
    else:
        print("Brawo! Odgadłeś liczbę!")

print("Koniec programu")