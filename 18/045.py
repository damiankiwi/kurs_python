x1, y1, r1, x2, y2, r2 = map(float, input("Podaj x1, y1, r1, x2, y2, r2 oddzielone spacją: ").split())

odleglosc_miedzy_srodkami = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

if odleglosc_miedzy_srodkami + r2 < r1:
    print("C2 jest w C1")
elif odleglosc_miedzy_srodkami + r1 < r2:
    print("C1 jest w C2")
elif odleglosc_miedzy_srodkami > r1 + r2:
    print("C1 i C2 nie nachodzą na siebie")
elif odleglosc_miedzy_srodkami == r1 + r2:
    print("Obwód C1 i C2 się zetknie")
else:
    print("Obwód C1 i C2 przecinają się")