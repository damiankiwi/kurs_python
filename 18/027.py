def find_progression_type_and_next_member(seq):
    if len(seq) != 3:
        return "Podaj sekwencję składającą się z trzech sukcesywnych elementów."

    a, b, c = seq

    if b - a == c - b:
        common_difference = b - a
        next_member = c + common_difference
        return f"Progresja arytmetyczna, następny element: {next_member}"

    elif b // a == c // b and b % a == c % b == 0:
        common_ratio = b // a
        next_member = c * common_ratio
        return f"Progresja geometryczna, następny element: {next_member}"

    else:
        return "Sekwencja nie jest ani progresją arytmetyczną, ani geometryczną."

user_sequence = [int(input(f"Podaj {i + 1}. element sekwencji: ")) for i in range(3)]

result = find_progression_type_and_next_member(user_sequence)
print(result)
