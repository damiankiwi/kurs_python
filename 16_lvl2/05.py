def deszyfruj_tekst(zaszyfrowany_tekst, przesuniecie):
    odszyfrowany_tekst = ""
    for litera in zaszyfrowany_tekst:
        if litera.isalpha():  #Sprawdzamy, czy znak jest literą
            if litera.isupper():  #Deszyfrujemy duże litery
                odszyfrowany_tekst += chr((ord(litera) - 65 - przesuniecie) % 26 + 65)
            elif litera.islower():  #Deszyfrujemy małe litery
                odszyfrowany_tekst += chr((ord(litera) - 97 - przesuniecie) % 26 + 97)
        else:
            odszyfrowany_tekst += litera  #Pozostawiamy pozostałe znaki bez zmian
    return odszyfrowany_tekst

#Pobieramy zaszyfrowany tekst od użytkownika
zaszyfrowany_tekst = input("Podaj tekst do odszyfrowania: ")

#Pobieramy przesunięcie od użytkownika
przesuniecie = int(input("Podaj wartość przesunięcia: "))

#Deszyfrujemy tekst
odszyfrowany_tekst = deszyfruj_tekst(zaszyfrowany_tekst, przesuniecie)

#Wyświetlamy odszyfrowany tekst
print("Odszyfrowany tekst:", odszyfrowany_tekst)