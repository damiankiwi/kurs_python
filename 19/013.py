def znajdz_napisy_z_prefixem(prefix, lista):
    napisy = [slowo for slowo in lista if slowo.startswith(prefix)]
    return napisy

input1 = ('ca', ['cat', 'car', 'fear', 'center'])
output1 = znajdz_napisy_z_prefixem(*input1)
print(f"Input:\n{input1}\nOutput:\n{output1}")

input2 = ('do', ['cat', 'dog', 'shatter', 'donut', 'at', 'todo'])
output2 = znajdz_napisy_z_prefixem(*input2)
print(f"\nInput:\n{input2}\nOutput:\n{output2}")