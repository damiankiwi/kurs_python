def czy_consecutive_similar(ciag):
    for i in range(len(ciag) - 1):
        if ciag[i] == ciag[i + 1]:
            return True
    return False

print("Oryginalny ciąg: PHP")
print("Sprawdzenie obecności kolejnych podobnych liter:", czy_consecutive_similar("PHP"))

print("Oryginalny ciąg: PHHP")
print("Sprawdzenie obecności kolejnych podobnych liter:", czy_consecutive_similar("PHHP"))

print("Oryginalny ciąg: PHPP")
print("Sprawdzenie obecności kolejnych podobnych liter:", czy_consecutive_similar("PHPP"))