from collections import Counter
import string

dlugi_tekst = """To jest przykładowy długi tekst. Tekst ten jest używany do demonstracji programu.
Chcemy znaleźć częstotliwość występowania każdego słowa w tym tekście. Ten program pomoże nam w tym zadaniu.
"""

tekst_bez_interpunkcji = dlugi_tekst.translate(str.maketrans('', '', string.punctuation))
slowa = tekst_bez_interpunkcji.lower().split()

czestotliwosc_slow = Counter(slowa)

for slowo, liczba in czestotliwosc_slow.items():
    print(f"{slowo}: {liczba}")