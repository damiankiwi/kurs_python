with open(__file__, 'r') as plik_zrodlowy:
    kod_zrodlowy = plik_zrodlowy.read()

with open("090_kopia_kodu.py", 'w') as plik_kopii:
    plik_kopii.write(kod_zrodlowy)

print("Utworzono kopię kodu źródłowego.")
