def indeksy_male_litery(ciag):
    return [i for i, char in enumerate(ciag) if char.islower()]

print("Oryginalny ciąg: Python")
print("Indeksy wszystkich małych liter w ciągu:", indeksy_male_litery("Python"))

print("Oryginalny ciąg: JavaScript")
print("Indeksy wszystkich małych liter w ciągu:", indeksy_male_litery("JavaScript"))

print("Oryginalny ciąg: PHP")
print("Indeksy wszystkich małych liter w ciągu:", indeksy_male_litery("PHP"))