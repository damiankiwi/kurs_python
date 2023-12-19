def sprawdz_obecnosc_liter(ciag1, ciag2):
    for litera in ciag2:
        if litera not in ciag1:
            return False
    return True

input1 = ["python", "ypth"]
output1 = sprawdz_obecnosc_liter(*input1)
print(f"Ciąg 1: {input1[0]}, Ciąg 2: {input1[1]}\nCzy litery drugiego ciągu są obecne w pierwszym: {output1}")

input2 = ["python", "ypths"]
output2 = sprawdz_obecnosc_liter(*input2)
print(f"Ciąg 1: {input2[0]}, Ciąg 2: {input2[1]}\nCzy litery drugiego ciągu są obecne w pierwszym: {output2}")

input3 = ["python", "ypthon"]
output3 = sprawdz_obecnosc_liter(*input3)
print(f"Ciąg 1: {input3[0]}, Ciąg 2: {input3[1]}\nCzy litery drugiego ciągu są obecne w pierwszym: {output3}")

input4 = ["123456", "01234"]
output4 = sprawdz_obecnosc_liter(*input4)
print(f"Ciąg 1: {input4[0]}, Ciąg 2: {input4[1]}\nCzy litery drugiego ciągu są obecne w pierwszym: {output4}")

input5 = ["123456", "1234"]
output5 = sprawdz_obecnosc_liter(*input5)
print(f"Ciąg 1: {input5[0]}, Ciąg 2: {input5[1]}\nCzy litery drugiego ciągu są obecne w pierwszym: {output5}")