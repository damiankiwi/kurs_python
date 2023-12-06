def dodaj_wiersze_i_kolumny(macierz):
    macierz_wynikowa = []

    for wiersz in macierz:
        macierz_wynikowa.append(wiersz + [sum(wiersz)])

    sumy_kolumn = [sum(kolumna) for kolumna in zip(*macierz)]
    macierz_wynikowa.append(sumy_kolumn + [sum(sumy_kolumn)])

    return macierz_wynikowa


def drukuj_macierz(macierz):
    for wiersz in macierz:
        print(" ".join(map(str, wiersz)))


def main():
    try:
        while True:
            rozmiar = int(input("Podaj liczbę wierszy/kolumn (0 aby zakończyć): "))
            if rozmiar == 0:
                break

            macierz = []
            print("Podaj wartości komórek:")
            for _ in range(rozmiar):
                wiersz = list(map(int, input().split()))
                macierz.append(wiersz)

            macierz_wynikowa = dodaj_wiersze_i_kolumny(macierz)

            print("Wynik:")
            drukuj_macierz(macierz_wynikowa)

    except ValueError:
        print("Nieprawidłowe dane. Podaj poprawną liczbę.")
    except EOFError:
        pass


if __name__ == "__main__":
    main()