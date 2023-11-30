while True:
    n = int(input("Podaj liczbę prostych (1 <= n <= 10000, 0 aby zakończyć): "))

    if n == 0:
        break

    regions = (n ** 2 + n + 2) // 2
    print(f"Liczba obszarów: {regions}")