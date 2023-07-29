import calendar

def main():
    try:
        miesiac = int(input("Podaj numer miesiąca (1-12): "))
        rok = int(input("Podaj rok: "))

        cal = calendar.month(rok, miesiac)
        print("Kalendarz dla {} {}: \n{}".format(calendar.month_name[miesiac], rok, cal))

    except ValueError:
        print("Nieprawidłowe dane. Podaj poprawny numer miesiąca (1-12) i rok.")

if __name__ == "__main__":
    main()