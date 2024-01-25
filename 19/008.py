def podziel_na_listy(tekst):
    slowa = tekst.split()
    slowa_lista = []
    separatory_lista = []

    for slowo in slowa:
        slowo = slowo.rstrip(',.')
        slowo = slowo.lstrip(',.')
        slowo = slowo.replace(',', ', ')
        slowa_lista.append(slowo)

    for i in range(1, len(slowa)):
        separator = tekst.find(slowa[i], tekst.find(slowa[i - 1]) + len(slowa[i - 1]))
        separatory_lista.append(tekst[len(slowa[i - 1]):separator])

    separatory_lista.append(tekst[tekst.rfind(slowa[-1]) + len(slowa[-1]):])

    return [slowa_lista, separatory_lista]

print(podziel_na_listy("W3resource Python, Exercises."))
print(podziel_na_listy("The dance, held in the school gym, ended at midnight."))
print(podziel_na_listy("The colors in my studyroom are blue, green, and yellow."))