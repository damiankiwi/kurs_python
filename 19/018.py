def znajdz_indeksy(macierz_nieregularna, cel):
    indeksy = []
    for i, wiersz in enumerate(macierz_nieregularna):
        for j, element in enumerate(wiersz):
            if element == cel:
                indeksy.append([i, j])
    return indeksy

input1 = ([ [1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19] ], 19)
output1 = znajdz_indeksy(*input1)
print(f"Wejście:\n{input1}\nWyjście:\n{output1}")

input2 = ([ [1, 2, 3, 2], [], [7, 9, 2, 1, 4] ], 2)
output2 = znajdz_indeksy(*input2)
print(f"\nWejście:\n{input2}\nWyjście:\n{output2}")