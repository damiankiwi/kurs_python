def znajdz_najwieksza_liczbe_z_przecinkiem(numbers):
    liczby = [float(liczba.replace(',', '.')) for liczba in numbers]
    return str(max(liczby))

liczby_wejsciowe = ['100', '102,1', '101.1']
wynik = znajdz_najwieksza_liczbe_z_przecinkiem(liczby_wejsciowe)
print(f"Wejście:\n{liczby_wejsciowe}\nWyjście:\n{wynik}")