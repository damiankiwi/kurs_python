# metodą iteracyjną ze wzoru definicyjnego: n! = 12...n,
# metodą rekurencyjną zgodnie z definicją: n! = n(n-1)! przy czym 0! = 1.

def iteracyjna_silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def rekurencyjna_silnia(n):
    if n == 0:
        return 1
    else:
        return n * rekurencyjna_silnia(n - 1)


n = int(input("Podaj liczbę: "))

silnia_iteracyjna = iteracyjna_silnia(n)
print(f"Silnia z {n} (metoda iteracyjna): {silnia_iteracyjna}")

silnia_rekurencyjna = rekurencyjna_silnia(n)
print(f"Silnia z {n} (metoda rekurencyjna): {silnia_rekurencyjna}")
