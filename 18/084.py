def licz_ujemne_i_sumuj_dodatnie(lista_liczb):
    liczba_ujemnych = sum(1 for num in lista_liczb if num < 0)
    suma_dodatnich = sum(num for num in lista_liczb if num > 0)
    return [liczba_ujemnych, suma_dodatnich]

input1 = [1, 2, 3, 4, 5]
output1 = licz_ujemne_i_sumuj_dodatnie(input1)
print(f"Oryginalna lista: {input1}\nLiczba liczb ujemnych i suma liczb dodatnich: {output1}")

input2 = [-1, -2, -3, -4, -5]
output2 = licz_ujemne_i_sumuj_dodatnie(input2)
print(f"Oryginalna lista: {input2}\nLiczba liczb ujemnych i suma liczb dodatnich: {output2}")

input3 = [1, 2, 3, -4, -5]
output3 = licz_ujemne_i_sumuj_dodatnie(input3)
print(f"Oryginalna lista: {input3}\nLiczba liczb ujemnych i suma liczb dodatnich: {output3}")

input4 = [1, 2, -3, -4, -5]
output4 = licz_ujemne_i_sumuj_dodatnie(input4)
print(f"Oryginalna lista: {input4}\nLiczba liczb ujemnych i suma liczb dodatnich: {output4}")