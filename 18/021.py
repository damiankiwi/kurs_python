def count_zeros_in_factorial(n):
    count = 0
    power_of_5 = 5

    while n // power_of_5 > 0:
        count += n // power_of_5
        power_of_5 *= 5

    return count

n = int(input("Podaj liczbę n: "))

if 1 <= n <= 2 * 10**9:
    result = count_zeros_in_factorial(n)
    print(f"Liczba zer na końcu silni {n}!: {result}")
else:
    print("Podana liczba musi być w zakresie od 1 do 2*10^9.")