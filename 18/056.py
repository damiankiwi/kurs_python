import re

while True:
    text = input("Podaj tekst zawierający liczby (0 aby zakończyć): ")

    if text == '0':
        break

    numbers = re.findall(r'\b\d+\b', text)
    total_sum = sum(map(int, numbers))

    print(f"Suma wartości liczbowych: {total_sum}")