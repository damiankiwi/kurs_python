def dlugosc_napisow(lista):
    dlugosci = [len(slowo) for slowo in lista]
    return dlugosci

input1 = ['cat', 'car', 'fear', 'center']
output1 = dlugosc_napisow(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
output2 = dlugosc_napisow(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")