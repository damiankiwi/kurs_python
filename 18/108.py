def sprawdz_sume_ostatnich_cyfr(liczba1, liczba2, liczba3):
    ostatnia_cyfra_liczby1 = abs(liczba1) % 10
    ostatnia_cyfra_liczby2 = abs(liczba2) % 10
    ostatnia_cyfra_liczby3 = abs(liczba3) % 10

    return (ostatnia_cyfra_liczby1 + ostatnia_cyfra_liczby2) == ostatnia_cyfra_liczby3


print(sprawdz_sume_ostatnich_cyfr(12, 26, 44))
print(sprawdz_sume_ostatnich_cyfr(145, 122, 1010))
print(sprawdz_sume_ostatnich_cyfr(0, 20, 40))
print(sprawdz_sume_ostatnich_cyfr(1, 22, 40))
print(sprawdz_sume_ostatnich_cyfr(145, 129, 104))