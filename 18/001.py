def czy_wszystkie_rozne(sekwencja):
    if len(sekwencja) == len(set(sekwencja)):
        return True
    else:
        return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 2, 3, 4]

wynik1 = czy_wszystkie_rozne(lista1)
wynik2 = czy_wszystkie_rozne(lista2)

print("Czy wszystkie liczby w liście 1 są różne?", wynik1)
print("Czy wszystkie liczby w liście 2 są różne?", wynik2)
