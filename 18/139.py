def znajdz_najblizszy_palindrom(liczba):
    def jest_palindromem(liczba_str):
        return liczba_str == liczba_str[::-1]

    i = 1
    while True:
        mniejszy = liczba - i
        wiekszy = liczba + i

        if jest_palindromem(str(mniejszy)):
            return mniejszy
        elif jest_palindromem(str(wiekszy)):
            return wiekszy

        i += 1

num1 = 120
print("Oryginalna liczba:", num1)
print("Najbliższy palindrom tej liczby:", znajdz_najblizszy_palindrom(num1))

num2 = 321
print("Oryginalna liczba:", num2)
print("Najbliższy palindrom tej liczby:", znajdz_najblizszy_palindrom(num2))

num3 = 43
print("Oryginalna liczba:", num3)
print("Najbliższy palindrom tej liczby:", znajdz_najblizszy_palindrom(num3))

num4 = 1234
print("Oryginalna liczba:", num4)
print("Najbliższy palindrom tej liczby:", znajdz_najblizszy_palindrom(num4))