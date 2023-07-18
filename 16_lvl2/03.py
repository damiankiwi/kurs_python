import random

def game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        print("Zgadnij, czy kolejna liczba będzie wyższa czy niższa niż", number)
        guess = input("wyższa/niższa: ").lower()

        if guess != "wyższa" and guess != "niższa":
            print("Niepoprawny wybór. Wybierz 'wyższa' lub 'niższa'.")
            continue

        next_number = random.randint(1, 100)
        attempts += 1

        print("Wylosowana liczba to:", next_number)

        if (guess == "wyższa" and next_number > number) or (guess == "niższa" and next_number < number):
            print("Gratulacje, wygrałeś!")
            break
        else:
            print("Niestety, przegrałeś. Kolejna liczba była", "wyższa" if next_number > number else "mniejsza", "niż", number)
            print("Liczba prób:", attempts)
            number = next_number

game()