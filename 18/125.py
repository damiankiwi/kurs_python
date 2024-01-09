def odwroc_ciag(ciag):
    return ciag.lower()[::-1]

print("Oryginalny ciąg: PHP")
print("Odwróć ciąg w małych literach:", odwroc_ciag("PHP"))

print("Oryginalny ciąg: JavaScript")
print("Odwróć ciąg w małych literach:", odwroc_ciag("JavaScript"))

print("Oryginalny ciąg: PHPP")
print("Odwróć ciąg w małych literach:", odwroc_ciag("PHPP"))