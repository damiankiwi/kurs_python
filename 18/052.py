def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_of_primes(n):
    primes_sum = 0
    count = 0
    current_num = 2

    while count < n:
        if is_prime(current_num):
            primes_sum += current_num
            count += 1
        current_num += 1

    return primes_sum


while True:
    n = int(input("Podaj liczbę (n <= 10000) do obliczenia sumy pierwszych n liczb pierwszych (0 aby zakończyć): "))

    if n == 0:
        break

    result = sum_of_primes(n)
    print(f"Suma pierwszych {n} liczb pierwszych: {result}")