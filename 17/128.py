def czy_sa_male_litery(tekst):
    for znak in tekst:
        if znak.islower():
            return True
    return False

przykladowy_tekst = "To jest Przykladowy TEKST"

if czy_sa_male_litery(przykladowy_tekst):
    print("W podanym tekście są małe litery.")
else:
    print("W podanym tekście nie ma małych liter.")
