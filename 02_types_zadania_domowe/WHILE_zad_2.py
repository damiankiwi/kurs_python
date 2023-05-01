#2. Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
# (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
user_num = int(input("Zgadnij ukrytą liczbę z od 0 do 20: "))
while user_num != secret_num:
    user_num = (int(input("Błędna liczba, spróbuj ponownie: ")))
print('Bingo trafiłeś! Prawidłowa liczba to', secret_num)

