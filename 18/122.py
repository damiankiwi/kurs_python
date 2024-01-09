def czy_same_litery(case):
    return case.islower() or case.isupper()

print("Oryginalny ciąg: PHP")
print("Coded string:", czy_same_litery("PHP"))

print("Oryginalny ciąg: javascript")
print("Coded string:", czy_same_litery("javascript"))

print("Oryginalny ciąg: JavaScript")
print("Coded string:", czy_same_litery("JavaScript"))