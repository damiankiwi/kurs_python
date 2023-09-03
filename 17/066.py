def oblicz_bmi(waga, wzrost):
    wzrost_metry = wzrost / 100
    bmi = waga / (wzrost_metry * wzrost_metry)
    return bmi

waga = float(input("Podaj wagę (w kilogramach): "))
wzrost = float(input("Podaj wzrost (w centymetrach): "))

bmi = oblicz_bmi(waga, wzrost)
print(f"Twoje BMI wynosi: {bmi:.2f}")
