def znajdz_dzielniki(liczba):
    dzielniki = {i for i in range(1, liczba + 1) if liczba % i == 0}
    return dzielniki

print("Oryginalna liczba: 1")
print("Dzielniki tej liczby:", znajdz_dzielniki(1))

print("Oryginalna liczba: 12")
print("Dzielniki tej liczby:", znajdz_dzielniki(12))

print("Oryginalna liczba: 100")
print("Dzielniki tej liczby:", znajdz_dzielniki(100))