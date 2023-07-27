def main():
    try:
        n = int(input("Podaj liczbę całkowitą n: "))

        wynik = n + (n * 10 + n) + (n * 100 + n * 10 + n)

        print("Wynik:", wynik)

    except ValueError:
        print("Nieprawidłowe dane. Podaj poprawną liczbę całkowitą.")

if __name__ == "__main__":
    main()