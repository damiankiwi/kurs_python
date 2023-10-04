start = 32  # Początkowy kod Unicode
end = 127   # Końcowy kod Unicode

for kod_unicode in range(start, end + 1):
    znak_unicode = chr(kod_unicode)
    print(f"Kod Unicode: {kod_unicode}, Znak: {znak_unicode}")