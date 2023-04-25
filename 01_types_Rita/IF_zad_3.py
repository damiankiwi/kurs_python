# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
# ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

"""Marta Ciemiorek 18:10
ocena1 = float(input("podaj ocenę"))
ocena2 = float(input("podaj ocenę"))
ocena3 = float(input("podaj ocenę"))

srednia = (ocena3 + ocena2 + ocena1)/3
if srednia >= 7:
    print("bardzo dobry")
elif  srednia <=4 :
    print("niewarta uwagi")
else:
    print("przecietna")"""


ocena1 = int(input("Podaj pierwszzą ocenę/opinie o książce w skali 1-10 -> "))
ocena2 = int(input("Podaj drugą ocenę/opinie o książce w skali 1-10 -> "))
ocena3 = int(input("Podaj trzecią ocenę/opinie o książce w skali 1-10 -> "))

srednia = (ocena1 + ocena2 + ocena3) //3
srednia = round(srednia, 3) # zaokraglenie

if srednia >= 7:
    print("very good")
elif srednia >= 4:
    print("not interesting")
else:
    print("bad")
