ciag_znakow = input("Podaj ciąg znaków: ")
odwrocony_ciag = ciag_znakow[::-1]
print("Odwrocony ciag znakow (string slicing):", odwrocony_ciag)

odwrocony_ciag = ""
for i in range(len(ciag_znakow) - 1, -1, -1):
    odwrocony_ciag += ciag_znakow[i]
print("Odwrocony ciag znakow (pętla for):", odwrocony_ciag)

odwrocony_ciag = ""
index = len(ciag_znakow) - 1
while index >= 0:
    odwrocony_ciag += ciag_znakow[index]
    index -= 1
print("Odwrocony ciag znakow (pętla while):", odwrocony_ciag)