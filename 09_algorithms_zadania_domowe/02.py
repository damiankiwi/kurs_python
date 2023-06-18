def sum_of_multiples(N):
    sum = 0
    for number in range(N):
        if number % 5 == 0 or number % 7 == 0:
            sum += number
    return sum

N = 21
result = sum_of_multiples(N)
print(f"Suma wszystkich wielokrotności 5 lub 7 poniżej liczby {N} wynosi: {result}")