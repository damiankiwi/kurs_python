import datetime

input_date = input("Podaj rok, miesiąc i dzień (oddzielone spacją): ")
year, month, day = map(int, input_date.split())

if 1 <= month <= 12 and 1 <= day <= 31:

    dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

    data = datetime.date(year, month, day)
    numer_dnia_tygodnia = data.weekday()

    print(f"Nazwa daty: {dni_tygodnia[numer_dnia_tygodnia]}")
else:
    print("Nieprawidłowa data.")