def znajdz_indeksy_spadku(liczby):
    return [i for i in range(1, len(liczby)) if liczby[i] < liczby[i-1]]

input1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
output1 = znajdz_indeksy_spadku(input1)
print(f"Wejście:\n{input1}\nWyjście:\n{output1}")

input2 = [6, 5, 4, 3, 2, 1]
output2 = znajdz_indeksy_spadku(input2)
print(f"\nWejście:\n{input2}\nWyjście:\n{output2}")

input3 = [1, 19, 5, 15, 5, 25, 5]
output3 = znajdz_indeksy_spadku(input3)
print(f"\nWejście:\n{input3}\nWyjście:\n{output3}")