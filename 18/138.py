def odwroc_binarna_i_konwertuj(liczba):
    binarna_rep = bin(liczba)[2:]
    odwrocona_binarna = binarna_rep[::-1]
    return int(odwrocona_binarna, 2)

num1 = 13
print("Oryginalna liczba:", num1)
print("Odwróć reprezentację binarną tej liczby i skonwertuj na liczbę całkowitą:", odwroc_binarna_i_konwertuj(num1))

num2 = 145
print("Oryginalna liczba:", num2)
print("Odwróć reprezentację binarną tej liczby i skonwertuj na liczbę całkowitą:", odwroc_binarna_i_konwertuj(num2))

num3 = 1342
print("Oryginalna liczba:", num3)
print("Odwróć reprezentację binarną tej liczby i skonwertuj na liczbę całkowitą:", odwroc_binarna_i_konwertuj(num3))