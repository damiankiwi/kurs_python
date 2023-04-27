#https://docs.python.org/3/library/stdtypes.html#string-methods

"""1. Jak sprawdzić że ciąg znaków zawiera tylko cyfry"""

"1234".isnumeric()
"1234".isdigit()

"""2. Wyświetlić tekst wypośrodkowany np “mata” -> “***mata***"""

”mata”.center(10, '*')

"""3. Jaka metoda usunie znaki tylko z prawej strony
Np. www.flynerd.pl -> wyrzucamy “w” i mamy “.flynerd.pl”"""

lalalaaaaaa".rstrip('a')
"www.flynerd.pl".lstrip('w')

"""4. Jak sprawdzić że tekst zawiera tylko duże litery np
“Abc” - nie
“ABC” - dobrze"""

>>> "ATCGGAGAGAATATATATA".isupper()
True
>>> not "ATCGGAGAGAATATATATA".islower()
True

"""5. Jak policzy wystąpienia podtekstu w tekście np.
Banana “na” -> 2"""

"banana".count('na')
2

"""6. Dla chętych ciąg składa się tylko z cyfr i liter i ma conajmniej 1 dużą literę 
“Abc” ✅ 
“123abC” ✅ 
“ab123cd” 🚫 
“abcd” 🚫 
“ABC” 🚫 
“12345” 🚫"""