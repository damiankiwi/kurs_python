def subtract_sum_of_digits(number):
    while number > 0:
        digit_sum = sum(map(int, str(number)))
        number -= digit_sum
        print(f"{number} (po odjęciu sumy cyfr: {digit_sum})")

positive_number = int(input("Podaj dodatnią liczbę: "))

if positive_number > 0:
    subtract_sum_of_digits(positive_number)
else:
    print("Podana liczba musi być dodatnia.")