def rozwiaz_rownanie(a, b, c, d, e, f):
    wyznacznik = a * e - b * d

    if wyznacznik != 0:
        x = (c * e - b * f) / wyznacznik
        y = (a * f - c * d) / wyznacznik
        return x, y
    else:
        return None

wejscie = input("Podaj wartości a, b, c, d, e, f oddzielone spacjami: ")
a, b, c, d, e, f = map(float, wejscie.split())

wynik = rozwiaz_rownanie(a, b, c, d, e, f)

if wynik:
    x, y = wynik
    print(f"Wartości x i y: {x:.3f} {y:.3f}")
else:
    print("Brak rozwiązania.")