def czy_samogloska(znak):
    samogloski = "aeiouAEIOU"
    if znak in samogloski:
        return True
    else:
        return False

podany_znak = input("Podaj znak: ")

if len(podany_znak) == 1:
    if czy_samogloska(podany_znak):
        print(f"{podany_znak} to samogłoska.")
    else:
        print(f"{podany_znak} to spółgłoska.")
else:
    print("Podaj dokładnie jeden znak.")