#6. Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

import random

def game_k_p_n():
    game_choice = ['k', 'p', 'n']

    print('Gra w kamień, papier oraz nożyce!')
    game_round = int(input('Podaj ilość rund w grze: '))
    print('Pamiętaj! Możesz przerwać grę w dowolonej chwili wpisując słowo "koniec" Powodzenia!')

    player_wins = 0
    computer_wins = 0

    while game_round > 0:
        player = input('Wybierz figurę: kamień (k),  papier(p),  nożyce(n): ')
        computer = random.choice(game_choice)

        if player == computer:
            print('Wybraliście te same figury! Remis!')
        elif player == 'n' and computer == 'p':
            print('Wygrywa gracz!')
            player_wins += 1
        elif player == 'p' and computer == 'k':
            print('Wygrywa gracz!')
            player_wins += 1
        elif player == 'k' and computer == 'n':
            print('Wygrywa gracz!')
            player_wins += 1
        elif player == 'p' and computer == 'n':
            print('Wygrywa komputer!')
            computer_wins += 1
        elif player == 'k' and computer == 'p':
            print('Wygrywa komputer!')
            computer_wins += 1
        elif player == 'n' and computer == 'k':
            print(f'Wygrywa komputer!')
            computer_wins += 1

        game_round -= 1
        if game_round == 0 and player_wins > computer_wins:
            print(f'Wygrałeś z komputerem {player_wins} do {computer_wins}!')
        elif game_round == 0 and computer_wins > player_wins:
            print(f'Przegrałeś z komputerem {computer_wins} do {player_wins}!')
        elif game_round == 0 and player_wins == computer_wins:
            print(f'Nieroztrzygnięta gra! Jest remis: {player_wins}:{computer_wins}!')

        if player == 'koniec':
            print(f'Zakończyłeś grę na własne życzenie, wynik: {player_wins}:{computer_wins}!')
            break

game_k_p_n()