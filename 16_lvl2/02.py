import random

def rzut_moneta():
    wynik = random.randint(0, 1)
    if wynik == 0:
        return "orzeł"
    else:
        return "reszka"

while True:
    print("Rzucam monetą... i wypadła", rzut_moneta() + "!")
    wybor = input("Chcesz rzucić monetą ponownie? (t/n): ")
    if wybor.lower() != 't':
        break

print("Dziękuję za grę!")