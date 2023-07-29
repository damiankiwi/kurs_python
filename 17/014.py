from datetime import date

def liczba_dni_pomiedzy_datami(data1, data2):
    roznica_dat = data2 - data1

    return roznica_dat.days

def main():
    data1 = date(2023, 7, 2)
    data2 = date(2023, 7, 29)

    liczba_dni = liczba_dni_pomiedzy_datami(data1, data2)

    print("Liczba dni między datami:", liczba_dni)

if __name__ == "__main__":
    main()