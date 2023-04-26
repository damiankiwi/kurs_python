"""Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość."""

w = input("Podaj wagę ->")
h = input("Podaj wzrost ->")

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

bmi = w / (h ** 2)
print("Your BMI is:", round(bmi, 2))

#17,0 - 18,49	niedowaga
if bmi <=18.49:
    print("niedowaga")
#18,5 – 24,9	waga normalna
elif bmi <=24.9:
    print("waga normalna")
#25,0 – 29,9	nadwaga
elif bmi <=29.9:
    print("nadwaga")
#30,0 – 34,9	otyłość I stopnia
elif bmi <=34.9:
    print("otyłość")
else:
    print("Jesteś poważnie otyły!")
