def czy_rownolegle(line1, line2):
    proporcjonalne = line1[0] * line2[1] == line2[0] * line1[1]

    return proporcjonalne

line1_1 = [2, 3, 4]
line1_2 = [2, 3, 8]
line2_1 = [2, 3, 4]
line2_2 = [4, -3, 8]

wynik1 = czy_rownolegle(line1_1, line1_2)
wynik2 = czy_rownolegle(line2_1, line2_2)

print(f"Linie {line1_1} i {line1_2} są równoległe: {wynik1}")
print(f"Linie {line2_1} i {line2_2} są równoległe: {wynik2}")