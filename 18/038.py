def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_up_to_n(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

n = int(input("Podaj liczbę n (1 <= n <= 999,999): "))

result = count_primes_up_to_n(n)
print(f"Liczba liczb pierwszych mniejszych lub równych {n}: {result}")