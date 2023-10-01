
liczby = [1, 15, 30, 45, 60, 75, 90, 105, 120]

podzielne_przez_15 = list(filter(lambda x: x % 15 == 0, liczby))

print("Liczby podzielne przez 15:", podzielne_przez_15)
