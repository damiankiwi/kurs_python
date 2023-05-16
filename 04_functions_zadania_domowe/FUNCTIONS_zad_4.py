# 4. Napisać funkcję, która wypisze wszystkie parzyste z przekazanej
# listy elementów (wykorzystać funkcje z pkt 2)

# user_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_if_even_number():
    counter = int(input('Ile liczb chcesz dodać do listy? '))

    number_list = []

    for i in range(counter):
        user_numbers = int(input('Podaj liczbę całkowitą: '))
        number_list.append(user_numbers)

    even_elements = []
    for i in number_list:
        if i % 2 == 0:
            even_elements.append(i)
    print("Wśród podanych liczb, liczbami parzystym są: ", even_elements)

check_if_even_number()

