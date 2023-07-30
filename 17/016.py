def oblicz_roznice(liczba):
    roznica = liczba - 17

    if liczba > 17:
        return 2 * abs(roznica)
    else:
        return roznica

podana_liczba = float(input("Podaj liczbę: "))

wynik = oblicz_roznice(podana_liczba)
print("Dwukrotność wartości bezwzględnej tej różnicy wynosi: ", wynik)