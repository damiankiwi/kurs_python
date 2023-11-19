def oblicz_kwote_zadluzenia(n):
    dlug = 100000
    odsetki = 0.05

    for _ in range(n):
        dlug += dlug * odsetki
        dlug = round(dlug, -3)

    return dlug

n = int(input("Podaj liczbę miesięcy: "))

kwota_zadluzenia = oblicz_kwote_zadluzenia(n)
zaokraglona_kwota = round(kwota_zadluzenia, -3)

print(f"Zaokrąglona kwota zadłużenia po {n} miesiącach: ${zaokraglona_kwota:,}")