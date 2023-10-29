def znajdz_trójki_sumujące_się_do_zera(tablica):
    wynik = []
    n = len(tablica)
    tablica.sort()

    for i in range(n - 2):
        if i > 0 and tablica[i] == tablica[i - 1]:
            continue

        lewy = i + 1
        prawy = n - 1

        while lewy < prawy:
            suma = tablica[i] + tablica[lewy] + tablica[prawy]
            if suma == 0:
                wynik.append([tablica[i], tablica[lewy], tablica[prawy]])
                while lewy < prawy and tablica[lewy] == tablica[lewy + 1]:
                    lewy += 1
                while lewy < prawy and tablica[prawy] == tablica[prawy - 1]:
                    prawy -= 1
                lewy += 1
                prawy -= 1
            elif suma < 0:
                lewy += 1
            else:
                prawy -= 1

    return wynik


tablica = [-1, 0, 1, 2, -1, -4]

wynik = znajdz_trójki_sumujące_się_do_zera(tablica)
print(wynik)