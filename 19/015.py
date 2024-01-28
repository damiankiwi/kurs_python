def znajdz_najdluzszy_napis(lista):
    najdluzszy = max(lista, key=len, default=None)
    return najdluzszy

input1 = ['cat', 'car', 'fear', 'center']
output1 = znajdz_najdluzszy_napis(input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
output2 = znajdz_najdluzszy_napis(input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")