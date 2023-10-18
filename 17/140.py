def int_na_bin(liczba, ilosc_bitow):
    binarny = format(liczba, f'0{ilosc_bitow}b')
    return binarny

x = 12
ilosc_bitow = 8

binarny_x = int_na_bin(x, ilosc_bitow)
print(binarny_x)
