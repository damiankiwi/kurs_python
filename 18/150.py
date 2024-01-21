def licz_pierwiastek_szescienny(liczba):
    kroki = 0
    while liczba >= 3:
        liczba = liczba ** (1/3)
        kroki += 1
    return kroki

print(licz_pierwiastek_szescienny(3))
print(licz_pierwiastek_szescienny(39))
print(licz_pierwiastek_szescienny(10000))