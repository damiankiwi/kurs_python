def konkatenacja_n_ciagow(*ciagi):
    wynik = ""
    for ciag in ciagi:
        wynik += ciag
    return wynik

ciag1 = "Hello, "
ciag2 = "world!"
ciag3 = " This is a Python program."

wynik_konkatenacji = konkatenacja_n_ciagow(ciag1, ciag2, ciag3)

print("Wynik konkatenacji:", wynik_konkatenacji)
