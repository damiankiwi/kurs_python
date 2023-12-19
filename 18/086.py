def licz_rownosci(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

input1 = (1, 1, 1)
output1 = licz_rownosci(*input1)
print(f"Liczby wejściowe: {input1}\nLiczba równych liczb: {output1}")

input2 = (1, 2, 2)
output2 = licz_rownosci(*input2)
print(f"Liczby wejściowe: {input2}\nLiczba równych liczb: {output2}")

input3 = (-1, -2, -3)
output3 = licz_rownosci(*input3)
print(f"Liczby wejściowe: {input3}\nLiczba równych liczb: {output3}")

input4 = (-1, -1, -1)
output4 = licz_rownosci(*input4)
print(f"Liczby wejściowe: {input4}\nLiczba równych liczb: {output4}")