def przelicz_na_dni_godziny_minuty_sekundy(sekundy):
    dni = sekundy // 86400
    reszta_sekundy = sekundy % 86400
    godziny = reszta_sekundy // 3600
    reszta_sekundy %= 3600
    minuty = reszta_sekundy // 60
    sekundy = reszta_sekundy % 60
    return dni, godziny, minuty, sekundy

sekundy = int(input("Podaj liczbę sekund: "))
czas = sekundy

dni, godziny, minuty, sekundy = przelicz_na_dni_godziny_minuty_sekundy(sekundy)
print(f"{czas} sekund to {dni} dni, {godziny} godzin, {minuty} minut i {sekundy} sekund.")
