def find_notes_for_amount(amount):
    available_notes = [500, 200, 100, 50, 20, 10]
    note_count = {}

    for note in available_notes:
        if amount >= note:
            count = amount // note
            note_count[note] = count
            amount -= count * note

    return note_count

amount = int(input("Podaj kwotę: "))
result = find_notes_for_amount(amount)

print("Liczba banknotów dla danej kwoty:")
for note, count in result.items():
    print(f"{note} zł: {count} sztuk")
