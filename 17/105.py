import os


srodowisko = os.environ
for klucz, wartosc in srodowisko.items():
    print(f"{klucz}: {wartosc}")