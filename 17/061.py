def przelicz_na_cale(odleglosc_w_stopach):
    return odleglosc_w_stopach * 12

def przelicz_na_jardy(odleglosc_w_stopach):
    return odleglosc_w_stopach / 3

def przelicz_na_mile(odleglosc_w_stopach):
    return odleglosc_w_stopach / 5280

odleglosc_w_stopach = float(input("Podaj odległość w stopach: "))

odleglosc_w_cale = przelicz_na_cale(odleglosc_w_stopach)
odleglosc_w_jardy = przelicz_na_jardy(odleglosc_w_stopach)
odleglosc_w_mile = przelicz_na_mile(odleglosc_w_stopach)

print(f"Odległość w calach: {odleglosc_w_cale:.2f}")
print(f"Odległość w jardach: {odleglosc_w_jardy:.2f}")
print(f"Odległość w milach: {odleglosc_w_mile:.6f}")
