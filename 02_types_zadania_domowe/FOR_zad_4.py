# 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).


liczba = int(input('Podaj liczbę naturalną, ale nie większą niż 8 -->'))
if liczba >8:
    print("Podana liczba jest większą niż 8")
else:
    k=1
    for i in range(1,(liczba+1)):
        k = k * i
        print('silnia z', i, "wynosi:",k)

