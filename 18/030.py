def reverse_and_add(num):
    def reverse_digits(n):
        return int(str(n)[::-1])

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    while not is_palindrome(num):
        reversed_num = reverse_digits(num)
        num += reversed_num

    return num

given_number = int(input("Podaj liczbę: "))
result = reverse_and_add(given_number)
print(f"Wynik: {result}")