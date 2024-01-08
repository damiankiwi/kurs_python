def zakoduj_ciag(oryginalny_ciag):
    kodowane_znaki = {'P': '9', 'T': '0', 'S': '1', 'H': '6', 'A': '8'}
    zakodowany_ciag = ''.join(kodowane_znaki.get(znak, znak) for znak in oryginalny_ciag)
    return zakodowany_ciag

print("Oryginalny ciąg: PHP")
print("Zakodowany ciąg:", zakoduj_ciag("PHP"))

print("Oryginalny ciąg: JAVASCRIPT")
print("Zakodowany ciąg:", zakoduj_ciag("JAVASCRIPT"))