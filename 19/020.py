def okresl_kierunek_monotonicznej_sekwencji(sekwencja):
    rosnaca = all(sekwencja[i] <= sekwencja[i + 1] for i in range(len(sekwencja) - 1))
    malejaca = all(sekwencja[i] >= sekwencja[i + 1] for i in range(len(sekwencja) - 1))

    if rosnaca and not malejaca:
        return "Rosnący."
    elif malejaca and not rosnaca:
        return "Malejący."
    else:
        return "Nie jest to monotoniczna sekwencja!"

input1 = [1, 2, 3, 4, 5, 6]
output1 = okresl_kierunek_monotonicznej_sekwencji(input1)
print(f"Wejście:\n{input1}\nWyjście:\n{output1}")

input2 = [6, 5, 4, 3, 2, 1]
output2 = okresl_kierunek_monotonicznej_sekwencji(input2)
print(f"\nWejście:\n{input2}\nWyjście:\n{output2}")

input3 = [19, 19, 5, 5, 5, 5, 5]
output3 = okresl_kierunek_monotonicznej_sekwencji(input3)
print(f"\nWejście:\n{input3}\nWyjście:\n{output3}")