def przelicz_na_psi(ciśnienie_kpa):
    psi = ciśnienie_kpa * 0.14503773773375
    return psi

def przelicz_na_mmHg(ciśnienie_kpa):
    mmHg = ciśnienie_kpa * 7.50061561303
    return mmHg

def przelicz_na_atm(ciśnienie_kpa):
    atm = ciśnienie_kpa * 0.00986923169314
    return atm

ciśnienie_kpa = float(input("Podaj ciśnienie w kilopaskalach (kPa): "))

psi = przelicz_na_psi(ciśnienie_kpa)
mmHg = przelicz_na_mmHg(ciśnienie_kpa)
atm = przelicz_na_atm(ciśnienie_kpa)

print(f"{ciśnienie_kpa} kPa to {psi:.2f} psi")
print(f"{ciśnienie_kpa} kPa to {mmHg:.2f} mmHg")
print(f"{ciśnienie_kpa} kPa to {atm:.6f} atm")
