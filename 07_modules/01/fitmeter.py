import bmi

def main():
    waga  = float(input("Podaj wage w kilogramach: "))
    wzrost = float(input("Podaj wzrost w centymatrach: "))
    print("Twoje podpowiedzi: ", bmi.calculate_bmi(waga, wzrost))

main()