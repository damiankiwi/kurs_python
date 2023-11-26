while True:
    n, s = map(int, input("Podaj liczbę kombinacji i ich sumę oddzielone spacją, wpisz 0 0 aby zakończyć: ").split())

    if n == 0 and s == 0:
        break

    count = 0

    for i in range(10 ** (n - 1), 10 ** n):
        digits = [int(digit) for digit in str(i)]

        if sum(digits) == s and len(set(digits)) == len(digits):
            count += 1

    print(count)