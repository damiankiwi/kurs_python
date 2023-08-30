def przelicz_na_sekundy(czas, jednostka):
    if jednostka == "sekundy":
        return czas
    elif jednostka == "minuty":
        return czas * 60
    elif jednostka == "godziny":
        return czas * 3600
    elif jednostka == "dni":
        return czas * 86400
    else:
        return "Nieznana jednostka czasu"

czas = float(input("Podaj ilość czasu: "))
jednostka = input("Podaj jednostkę czasu (sekundy/minuty/godziny/dni): ")

czas_w_sekundach = przelicz_na_sekundy(czas, jednostka)
print(f"{czas} {jednostka} to {czas_w_sekundach:.2f} sekundy")
