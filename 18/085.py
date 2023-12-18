def czy_izogram(slowo):
    return len(slowo) == len(set(slowo))

input1 = "w3resource"
output1 = czy_izogram(input1)
print(f"Tekst wejściowy: {input1}\nCzy to jest izogram: {output1}")

input2 = "w3r"
output2 = czy_izogram(input2)
print(f"Tekst wejściowy: {input2}\nCzy to jest izogram: {output2}")

input3 = "Python"
output3 = czy_izogram(input3)
print(f"Tekst wejściowy: {input3}\nCzy to jest izogram: {output3}")

input4 = "Java"
output4 = czy_izogram(input4)
print(f"Tekst wejściowy: {input4}\nCzy to jest izogram: {output4}")