"""4. Utwórz zmienną przechowującą dowolny ciąg znaków.
Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis."""

znaki = input("Podaj ciąg znaków -> ")

if "a" in znaki:
    print('Ciąg zawiera literę a')
if len(znaki) < 5:
    print('Ciąg znaków jest za krótki, nie zawiera pięciu znaków')

else:
    print('Ciąg zawiera pięć znaków')


zamiana = znaki.replace('a', 'z')
print(zamiana)


