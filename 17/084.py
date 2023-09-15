def licz_wystapienia_znaku(tekst, znak):
    licznik = 0
    for litera in tekst:
        if litera == znak:
            licznik += 1
    return licznik

tekst = "Przykład tekstu z kilkoma literami 'a'."

znak_do_zliczenia = 'a'

liczba_wystapien = licz_wystapienia_znaku(tekst, znak_do_zliczenia)

print(f"Znak '{znak_do_zliczenia}' występuje {liczba_wystapien} razy w tekście.")
