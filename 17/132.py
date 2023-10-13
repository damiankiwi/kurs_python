import os

katalog_domowy = os.path.expanduser("~")
nazwa_uzytkownika = os.path.basename(katalog_domowy)

print("Katalog domowy użytkownika", nazwa_uzytkownika, "to:", katalog_domowy)
