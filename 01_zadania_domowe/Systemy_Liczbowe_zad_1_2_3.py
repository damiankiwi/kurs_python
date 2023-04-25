"""1. Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie.
Sprawdź czy to samo zwróci Python."""

#Binarnie
dec = 35
print(bin(dec), 'w systemie 2-owym')

#osemkowo
print(oct(dec), 'w systemie 8-owym')
#szesnastkwo
print(hex(dec), 'w systemie 16-owym')

"""2. Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. 
Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej)."""

bin_num = 1001111

print("liczba w systemie dwójkowym bin_num wynopsi:", (1*2**0)+(1*2**1)+(1*2**2)+(1*2**3)+(0*2**4)+(0*2**5)+(1*2**6))

"""3. Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym."""

hex_num = 0x1DB
print(hex_num)

oct_num = 0o2063
print(oct_num)