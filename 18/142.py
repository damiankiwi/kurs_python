def sprawdz_ciagi(ciag):
    i = 0
    while i < len(ciag):
        zeros, ones = 0, 0

        while i < len(ciag) and ciag[i] == '0':
            zeros += 1
            i += 1

        while i < len(ciag) and ciag[i] == '1':
            ones += 1
            i += 1

        if zeros != ones:
            return False

    return True

ciag1 = "001011"
print("Oryginalny ciąg:", ciag1)
print("Sprawdź, czy każdy sekwencyjny ciąg zer jest poprzedzony sekwencyjnym ciągiem jedynek:", sprawdz_ciagi(ciag1))

ciag2 = "01010101"
print("Oryginalny ciąg:", ciag2)
print("Sprawdź, czy każdy sekwencyjny ciąg zer jest poprzedzony sekwencyjnym ciągiem jedynek:", sprawdz_ciagi(ciag2))

ciag3 = "00"
print("Oryginalny ciąg:", ciag3)
print("Sprawdź, czy każdy sekwencyjny ciąg zer jest poprzedzony sekwencyjnym ciągiem jedynek:", sprawdz_ciagi(ciag3))

ciag4 = "000111000111"
print("Oryginalny ciąg:", ciag4)
print("Sprawdź, czy każdy sekwencyjny ciąg zer jest poprzedzony sekwencyjnym ciągiem jedynek:", sprawdz_ciagi(ciag4))

ciag5 = "00011100011"
print("Oryginalny ciąg:", ciag5)
print("Sprawdź, czy każdy sekwencyjny ciąg zer jest poprzedzony sekwencyjnym ciągiem jedynek:", sprawdz_ciagi(ciag5))

ciag6 = "0011101"
print("Oryginalny ciąg:", ciag6)
print("Sprawdź, czy każdy sekwencyjny ciąg zer jest poprzedzony sekwencyjnym ciągiem jedynek:", sprawdz_ciagi(ciag6))