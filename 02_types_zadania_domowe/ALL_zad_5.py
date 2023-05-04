# 5. Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

computer = random.randrange(1, 100)
print(computer)
game_chances = 6

while game_chances > 0:
    player = int(input('Podaj liczbę od 1 do 100: '))
    game_chances -= 1
    if player == computer:
        print(f'Zgadłeś. Komputer wylosował liczbę: {computer}')
        break
        # abs() - "absolute value", czyli wyznaczanie wartości bezwzględnej.
        # Po wprowadzeniu parametru liczbowego, zwracana jest jej wartość bezwzględna,
        # czyli zignorowanie znaku podanej liczby (ujemna stanie się dodatnią).
    elif abs(computer - player) > 20:
        print(f'Bardzo zimno! Masz jeszcze {game_chances}/6 szans ')
    elif abs(computer - player) > 10:
        print(f'Zimno! Masz jeszcze {game_chances}/6 szans ')
    elif abs(computer - player) > 5:
        print(f'Cieplej! Masz jeszcze {game_chances}/6 szans ')
    elif abs(computer - player) > 3:
        print(f'Bardzo ciepło! Masz jeszcze {game_chances}/6 szans ')
    else:
        print(f'Gorąco! Masz jeszcze {game_chances}/6 szans ')

    if game_chances == 0:
        print(f'Koniec gry, skończyły się Tobie szanse, Komputer wylosował liczbę: {computer}')
