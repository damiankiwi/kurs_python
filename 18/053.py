def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_partitions(even_num):
    combinations = 0
    for i in range(2, even_num // 2 + 1):
        if is_prime(i) and is_prime(even_num - i):
            combinations += 1
    return combinations


while True:
    even_num = int(input("Podaj liczbę parzystą (>=4, 0 aby zakończyć): "))

    if even_num == 0:
        break

    if even_num < 4 or even_num % 2 != 0:
        print("Podana liczba nie jest odpowiednia.")
        continue

    result = goldbach_partitions(even_num)
    print(f"Liczba kombinacji: {result}")