number = input("Podaj liczbę utworzoną z 8 cyfr od 0 do 9: ")

sorted_number = ''.join(sorted(number))
smallest = int(sorted_number)
largest = int(sorted_number[::-1])

difference = largest - smallest

print(f"Różnica między największą a najmniejszą liczbą: {difference}")