import random
import os

print("Witaj w grze wisielec")
print("Kategorie: \n1. animals \n2. fruits")

def words_input():
    filename = input('Podaj nazwe kategorii (bez rozszerzenia txt): ')
    if os.path.isfile(f'{filename}.txt'):
        with open(f'{filename}.txt', encoding = 'utf-8') as f:

            load_words = f.read().splitlines()
        return load_words
    else:
        print('Nie ma takiej kategori :(')

def read_words(filename) -> list:
    with open(filename, encoding = 'utf-8') as fp:
        content = fp.read().splitlines()
    return content

words_game = words_input()
if words_game is None:
    exit()

words_ask = []
words_list = []
game_chances = 6


def generate(words_to_generate):
    guess = random.choice(words_to_generate)
    words = [guess]
    for i in range(len(words[0])):
        words_list.append(words[0][i])
    for i in range(len(words[0])):
        words_ask.append('-')
    return guess

secret_word = generate(words_game)
print(secret_word) #wyświetla do sprawdzenia działania kodu

def game(guess_word, game_chances):
    print('Długość słowa', len(words_ask))
    while game_chances > 0:
        letter = (input(f'Podaj literę lub słowo aby odgadnąć hasło, masz {game_chances} szans: '))
        letter = letter.lower()
        game_chances -= 1
        if letter == guess_word:
            print('ZGADŁEŚ HASŁO PO SŁOWIE GRATULACJE, wylosowane hasło to:', guess_word)
            break

        else:
            for x in range(len(words_list)):
                if words_list[x] == letter:
                     words_ask[x] = letter

            print(words_ask)
            if words_ask == words_list:
                print('Hasło odgadnięte, wylosowane hasło to:', guess_word)
                break

            if game_chances == 0:
                print('Koniec gry, skończyły się Tobie szanse, hasło to :', guess_word)


game(secret_word, game_chances)