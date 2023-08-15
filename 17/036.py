def dodaj_liczby(a, b):
    if isinstance(a, int) and isinstance(b, int):
        suma = a + b
        return suma
    else:
        return "Oba obiekty nie są liczbami całkowitymi."

obiekt_a = input("Podaj pierwszy obiekt: ")
obiekt_b = input("Podaj drugi obiekt: ")

try:
    wynik = dodaj_liczby(int(obiekt_a), int(obiekt_b))
    print(f"Wynik dodawania: {wynik}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj dwie liczby całkowite.")
