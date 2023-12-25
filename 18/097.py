def find_highest_and_lowest(numbers_str):
    numbers = list(map(int, numbers_str.split()))

    if not numbers:
        return None

    highest = max(numbers)
    lowest = min(numbers)

    return highest, lowest


# Przykłady użycia
input1 = "1 4 5 77 9 0"
input2 = "-1 -4 -5 -77 -9 0"
input3 = "0 0"

output1 = find_highest_and_lowest(input1)
output2 = find_highest_and_lowest(input2)
output3 = find_highest_and_lowest(input3)

print(f"Oryginalny ciąg: {input1}\nNajwyższa i najniższa liczba w podanym ciągu: {output1}")
print(f"Oryginalny ciąg: {input2}\nNajwyższa i najniższa liczba w podanym ciągu: {output2}")
print(f"Oryginalny ciąg: {input3}\nNajwyższa i najniższa liczba w podanym ciągu: {output3}")