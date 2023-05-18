# 5. Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random

game_chances = 6
def game_warm_cold(game_chances):
    computer = random.randrange(1, 100)
    print(computer)

    while game_chances > 0:
            player = int(input('Podaj liczbę od 1 do 100: '))
            game_chances -= 1
            if player == computer:
                print(f'Zgadłeś. Komputer wylosował liczbę: {computer}')
                break

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

game_warm_cold(game_chances)
