def identyfikuj_i_wypisz_niepierwsze(minimum, maximum):
    print(f"Niepierwsze liczby od {minimum} do {maximum}:")

    for liczba in range(minimum, maximum + 1):
        if liczba > 1:
            for i in range(2, int(liczba**0.5) + 1):
                if liczba % i == 0:
                    print(liczba)
                    break

identyfikuj_i_wypisz_niepierwsze(1, 100)