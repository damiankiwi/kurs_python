def licz_zera_jedynki(liczba):
    binarna_rep = bin(liczba)[2:]
    liczba_zer = binarna_rep.count('0')
    liczba_jedynek = binarna_rep.count('1')
    return liczba_zer, liczba_jedynek

print("Oryginalna liczba: 12")
zeros, ones = licz_zera_jedynki(12)
print("Liczba zer i jedynek w reprezentacji binarnej tej liczby: Liczba zer:", zeros, ", Liczba jedynek:", ones)

print("Oryginalna liczba: 1234")
zeros, ones = licz_zera_jedynki(1234)
print("Liczba zer i jedynek w reprezentacji binarnej tej liczby: Liczba zer:", zeros, ", Liczba jedynek:", ones)