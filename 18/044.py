while True:
    n = int(input("Podaj liczbę elementów ciągu (0 aby zakończyć): "))

    if n == 0:
        break

    sequence = list(map(int, input("Podaj liczby oddzielone spacją: ").split()))

    max_sum = sequence[0]
    current_sum = sequence[0]

    for i in range(1, n):
        current_sum = max(sequence[i], current_sum + sequence[i])
        max_sum = max(max_sum, current_sum)

    print("Maksymalna suma ciągłego podciągu:", max_sum)