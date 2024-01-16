def odwroc_wyrazy_nieparzystej_dlugosci(ciag):
    slowa = ciag.split()
    nowe_slowa = [slowo[::-1] if len(slowo) % 2 != 0 else slowo for slowo in slowa]
    return ' '.join(nowe_slowa)

print("Oryginalny ciąg: The quick brown fox jumps over the lazy dog")
print("Odwroć wszystkie wyrazy o nieparzystej długości w ciągu:", odwroc_wyrazy_nieparzystej_dlugosci("The quick brown fox jumps over the lazy dog"))

print("Oryginalny ciąg: Python Exercises")
print("Odwroć wszystkie wyrazy o nieparzystej długości w ciągu:", odwroc_wyrazy_nieparzystej_dlugosci("Python Exercises"))