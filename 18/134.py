def zmiana_wielkosci_litery(ciag):
    nowy_ciag = ''
    for i, char in enumerate(ciag):
        if i % 2 == 0:
            nowy_ciag += char.upper()
        else:
            nowy_ciag += char.lower()
    return nowy_ciag

print("Oryginalny ciąg: Python Exercises")
print("Po zmianie wielkości liter w ciągu:", zmiana_wielkosci_litery("Python Exercises"))

print("Oryginalny ciąg: C# is used to develop web apps, desktop apps, mobile apps, games and much more.")
print("Po zmianie wielkości liter w ciągu:", zmiana_wielkosci_litery("C# is used to develop web apps, desktop apps, mobile apps, games and much more."))