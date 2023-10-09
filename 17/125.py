collection = [3, 5, 7, 'tekst', 2, 8, 'inne']

liczba_liczb = sum(isinstance(item, (int, float)) for item in collection)

print("Liczba liczb w kolekcji:", liczba_liczb)
