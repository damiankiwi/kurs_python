def szyfruj_tekst(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for litera in tekst:
        if litera.isalpha():  #Sprawdzamy, czy znak jest literą
            if litera.isupper():  #Szyfrujemy duże litery
                zaszyfrowany_tekst += chr((ord(litera) - 65 + przesuniecie) % 26 + 65)
            elif litera.islower():  #Szyfrujemy małe litery
                zaszyfrowany_tekst += chr((ord(litera) - 97 + przesuniecie) % 26 + 97)
        else:
            zaszyfrowany_tekst += litera  #Pozostawiamy pozostałe znaki bez zmian
    return zaszyfrowany_tekst

#Pobieramy tekst od użytkownika
tekst_do_zaszyfrowania = input("Podaj tekst do zaszyfrowania: ")

#Pobieramy przesunięcie od użytkownika
przesuniecie = int(input("Podaj wartość przesunięcia: "))

#Szyfrujemy tekst
zaszyfrowany_tekst = szyfruj_tekst(tekst_do_zaszyfrowania, przesuniecie)

#Wyświetlamy zaszyfrowany tekst
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)