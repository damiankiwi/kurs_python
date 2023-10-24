def sum_of_cubes(n):
    if n <= 0:
        return 0
    return sum(i**3 for i in range(1, n))

n = int(input("Podaj liczbę całkowitą dodatnią: "))
result = sum_of_cubes(n)
print(f"Suma sześcianów liczb mniejszych od {n} wynosi {result}")
