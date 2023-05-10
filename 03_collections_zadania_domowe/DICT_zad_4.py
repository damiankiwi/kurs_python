# 4. Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

"""Brzydko wyświetla wynik, liczby nie są w kolumnach jedna pod drugą"""
# for a in range(1, 11):
#     for b in range(1, 11):
#         print((a * b), end=" ")
#     print()

"""str.format() -- ‘{} {}’.format(a, b) -- Format strings in < Python 3.6"""
# for a in range(1, 11):
#     for b in range(1, 11):
#         print("{:3}".format(a * b), end=" ")
#     print()

"""F-Strings -- f'{a} {b}’ -- Format strings in Python 3.6+"""
for a in range(1, 11):
    for b in range(1, 11):
        print(f'{a*b:3}', end=" ")
    print()

# 1. % Operator -- ‘%s %s’ % (a, b) -- Old method. Don’t use it anymore!
# 2. str.format() -- ‘{} {}’.format(a, b) -- Format strings in < Python 3.6
# 3. F-Strings -- f'{a} {b}’ -- Format strings in Python 3.6+
# 4. Template Strings -- Template(‘$a $b’).substitute(a=a, b=b) -- Format user-supplied strings