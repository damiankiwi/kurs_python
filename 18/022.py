def generate_sequence(n):
    sequence = [1, 1, 1, 1]

    for i in range(4, n):
        next_term = sum(sequence[-4:])
        sequence.append(next_term)

    return sequence

N = int(input("Podaj wartość N: "))
result_sequence = generate_sequence(N)

print(f"Sekwencja do {N}-tego elementu:")
print(result_sequence)
print(f"{N}-ty element sekwencji: {result_sequence[N-1]}")