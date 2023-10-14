
wejscie = input("Wprowadź dwie liczby całkowite oddzielone spacją: ")


liczby = wejscie.split()

if len(liczby) == 2:
    liczba1, liczba2 = map(int, liczby)
    print("Pierwsza liczba:", liczba1)
    print("Druga liczba:", liczba2)
else:
    print("Wprowadź dokładnie dwie liczby całkowite oddzielone spacją.")
