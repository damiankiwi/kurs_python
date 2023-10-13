
dlugi_tekst = "To jest przykładowy tekst o zmiennej dlugosci."

if len(dlugi_tekst) < 10:
    zmienna1 = dlugi_tekst
elif len(dlugi_tekst) < 20:
    zmienna1, zmienna2 = dlugi_tekst.split(" ", 1)
else:
    zmienna1, zmienna2, zmienna3 = dlugi_tekst.split(" ", 2)

print("Zmienna 1:", zmienna1)
if 'zmienna2' in locals():
    print("Zmienna 2:", zmienna2)
if 'zmienna3' in locals():
    print("Zmienna 3:", zmienna3)
