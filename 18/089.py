def suma_trzech_najnizszych(lista):
    dodatnie = [liczba for liczba in lista if liczba > 0]
    dodatnie.sort()
    suma = sum(dodatnie[:3])
    return suma

input1 = [10, 20, 30, 40, 50, 60, 7]
output1 = suma_trzech_najnizszych(input1)
print(f"Oryginalna lista liczb: {input1}\nSuma trzech najniższych dodatnich liczb: {output1}")

input2 = [1, 2, 3, 4, 5]
output2 = suma_trzech_najnizszych(input2)
print(f"Oryginalna lista liczb: {input2}\nSuma trzech najniższych dodatnich liczb: {output2}")

input3 = [0, 1, 2, 3, 4, 5]
output3 = suma_trzech_najnizszych(input3)
print(f"Oryginalna lista liczb: {input3}\nSuma trzech najniższych dodatnich liczb: {output3}")