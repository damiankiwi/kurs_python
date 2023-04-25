"""2. Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika."""

trasa = float(input("Podaj długość trasy ->"))
cena_benzyny = float(input("Podaj cenę benzyny ->"))
spalanie_100km = float(input("Podaj średnie spalanie na 100km ->"))

koszt = spalanie_120km = ((trasa * spalanie_100km) / 100) * cena_benzyny

print("Koszt wyprawy wynosi:", (koszt))

