def znajdz_max_i_min(sekwencja):
    if len(sekwencja) == 0:
        return None, None

    max_liczba = min_liczba = sekwencja[0]

    for liczba in sekwencja:
        if liczba > max_liczba:
            max_liczba = liczba
        if liczba < min_liczba:
            min_liczba = liczba

    return max_liczba, min_liczba

liczby = [7, 2, 9, 1, 5, 10]
max_wartosc, min_wartosc = znajdz_max_i_min(liczby)

print("Maksymalna wartość:", max_wartosc)
print("Minimalna wartość:", min_wartosc)
