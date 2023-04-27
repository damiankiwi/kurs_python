"""6. Zapytaj użytkownika o numer od 1 do 100,
jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
w przeciwnym razie wyświetl “pudło!”."""

quessnumber = float(input("Zgadnij liczbę od 1 do 100 ->"))

number = 66

if quessnumber == number:
    print("gratulacje!")
else:
    print("pudło!")