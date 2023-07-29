import math

def objetosc_kuli(promien):
    objetosc = (4/3) * math.pi * promien**3
    return objetosc

def main():
    try:
        promien = float(input("Podaj promień kuli: "))

        objetosc = objetosc_kuli(promien)

        print("Objętość kuli o promieniu {} wynosi: {:.2f}".format(promien, objetosc))

    except ValueError:
        print("Nieprawidłowe dane. Podaj poprawną wartość liczbową jako promień kuli.")

if __name__ == "__main__":
    main()