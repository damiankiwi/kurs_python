import random
import os
from graphic import hangman_graphics  # opcja grafiki z pliku

print("Witaj w grze wisielec")
print("Kategorie: \n1. animals \n2. fruits")


def words_input():
    while True:
        filename = input('Podaj nazwe kategorii (bez rozszerzenia txt): ')
        if os.path.isfile(f'{filename}.txt'):
            with open(f'{filename}.txt', encoding='utf-8') as f:
                load_words = f.read().splitlines()
            return load_words
        else:
            print('Nie ma takiej kategorii :(')


def generate(words_to_generate):
    guess = random.choice(words_to_generate)
    words = [guess]
    words_list = list(guess)
    words_ask = ['-'] * len(words_list)
    return guess, words_list, words_ask


def main(guess_word, game_chances):
    print('Długość słowa:', len(words_ask))
    stage = 0
    while game_chances > 0:
        letter = input(f'Podaj literę lub słowo aby odgadnąć hasło, masz {game_chances} szans: ').lower()
        game_chances -= 1
        if letter == guess_word:
            print('ZGADŁEŚ HASŁO PO SŁOWIE GRATULACJE, wylosowane hasło to:', guess_word)
            break
        else:
            found = False
            for i, char in enumerate(words_list):
                if char == letter:
                    words_ask[i] = letter
                    found = True

            print(words_ask)
            if words_ask == words_list:
                print('Hasło odgadnięte, wylosowane hasło to:', guess_word)
                break
            elif not found:
                print(hangman_graphics[stage])
                stage += 1

            if stage == 6:
                print('Koniec gry, skończyły Ci się życia, hasło to:', guess_word)
                break
            if game_chances == 0:
                print('Koniec gry, skończyły Ci się szanse, hasło to:', guess_word)
                break


if __name__ == '__main__':
    try:
        words_game = words_input()
        if words_game is None:
            exit()
        secret_word, words_list, words_ask = generate(words_game)
        print(secret_word)  # wyświetla do sprawdzenia działania kodu
        main(secret_word, game_chances=10)
    except FileNotFoundError:
        print('Nie znaleziono pliku z daną kategorią.')