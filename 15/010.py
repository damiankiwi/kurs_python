def suma_liczb_nieparzystych():
    suma = 0
    liczba = 1

    while liczba <= 100:
        if liczba % 2 != 0:
            suma += liczba
        liczba += 1

    return suma

wynik = suma_liczb_nieparzystych()
print(f"Suma liczb nieparzystych z zakresu od 1 do 100 wynosi: {wynik}")