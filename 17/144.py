
zmienna = 42

if isinstance(zmienna, int):
    print("Zmienna jest liczbą całkowitą.")
elif isinstance(zmienna, str):
    print("Zmienna jest ciągiem znaków (string).")
else:
    print("Zmienna nie jest ani liczbą całkowitą, ani stringiem.")
