# 1. Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą
# bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.


""""stary kod bmi"""
# w = input("Podaj wagę ->")
# h = input("Podaj wzrost ->")
#
# w = float(w.replace(",", "."))
# h = float(h.replace(",", "."))
#
# bmi = w / (h ** 2)
# print("Your BMI is:", round(bmi, 2))
#
# #17,0 - 18,49	niedowaga
# if bmi <=18.49:
#     print("niedowaga")
# #18,5 – 24,9	waga normalna
# elif bmi <=24.9:
#     print("waga normalna")
# #25,0 – 29,9	nadwaga
# elif bmi <=29.9:
#     print("nadwaga")
# #30,0 – 34,9	otyłość I stopnia
# elif bmi <=34.9:
#     print("otyłość")
# else:
#     print("Jesteś poważnie otyły!")
""""stary kod bmi"""


def bmi_calc():
    w = int(input("Podaj wagę w kg ->"))
    h_cm = int(input("Podaj wzrost w cm ->"))
    h_m = h_cm / 100
    bmi = w / (h_m ** 2)
    print("Twoje BMI to:", bmi)
    return bmi

def bmi_list(bmi):

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

bmi = bmi_calc()
bmi_list(bmi)
