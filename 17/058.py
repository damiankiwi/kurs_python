def suma_pierwszych_n_liczb(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

n = int(input("Podaj liczbę n: "))
wynik = suma_pierwszych_n_liczb(n)
print(f"Suma pierwszych {n} liczb całkowitych: {wynik}")
