
string1 = "Hello, world!"
string2 = "Hello, world!"

if id(string1) == id(string2):
    print("Obie zmienne wskazują na ten sam obszar pamięci.")
else:
    print("Zmienne wskazują na różne obszary pamięci.")

