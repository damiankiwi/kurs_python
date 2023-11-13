def znajdz_ciag(trzeci_element, trzeci_od_konca_element, suma_ciagu):
    dlugosc_ciagu = (2 * suma_ciagu) // (trzeci_element + trzeci_od_konca_element)

    roznica_arytmetyczna = (trzeci_od_konca_element - trzeci_element) // (dlugosc_ciagu - 5)

    ciag = [i for i in range(trzeci_element, trzeci_od_konca_element + roznica_arytmetyczna, roznica_arytmetyczna)]

    return dlugosc_ciagu, ciag

trzeci_element = int(input("Podaj trzeci element ciągu: "))
trzeci_od_konca_element = int(input("Podaj trzeci od końca element: "))
suma_ciagu = int(input("Podaj sumę ciągu: "))

dlugosc, ciag = znajdz_ciag(trzeci_element, trzeci_od_konca_element, suma_ciagu)

print(f"Długość ciągu: {dlugosc}")
print("Ciąg:")
print(" ".join(map(str, ciag)))