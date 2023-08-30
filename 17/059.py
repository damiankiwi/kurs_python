def przelicz_na_centymetry(stopy, cale):
    wzrost_w_calach = stopy * 12 + cale
    wzrost_w_centymetrach = wzrost_w_calach * 2.54
    return wzrost_w_centymetrach

stopy = int(input("Podaj wzrost w stopach: "))
cale = int(input("Podaj wzrost w calach: "))

wzrost_centymetry = przelicz_na_centymetry(stopy, cale)
print(f"Wzrost {stopy} stóp i {cale} cali to {wzrost_centymetry:.2f} centymetrów")
