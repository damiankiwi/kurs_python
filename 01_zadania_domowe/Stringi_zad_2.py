"""2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3,
dołączając s2 w środku s1."""

#s1 = "laptop"
#s2 = "down"
s1 = input("Podaj pierwszy wyraz ->")
s2 = input("Podaj drugi wyraz ->")

ilosc_liter = len(s1)

#Funkcja len() informuje nas z jak wielu znaków składa się wyraz, dzielimy go na połowę // 2
string1 = slice(0, len(s1)//2)
string2 = slice(len(s1)//2, len(s1))
"""print(s1[string1], s1[string2])""" #podzielony wyraz na pół

s3 =(s1[string1] + s2 + s1[string2])
print(s3)







