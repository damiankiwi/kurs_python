# ilość: 4
# Lipski
# Kowal
# Adamiak
# Wojtczak

n = int(input('podaj liczbę nazwisk: '))  # Odczytaj liczbę nazwisk

names = []
for _ in range(n):
    name = input('podaj nazwisko:' )  # Odczytaj nazwisko
    names.append(name)

names.sort()  # Posortuj nazwiska leksykograficznie

for name in names:
    print(name)  # Wyświetl posortowane nazwiska