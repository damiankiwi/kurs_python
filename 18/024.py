def count_divisors(number, parity):
    divisors_count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            if parity == "even" and i % 2 == 0:
                divisors_count += 1
            elif parity == "odd" and i % 2 != 0:
                divisors_count += 1

    return divisors_count

integer_input = int(input("Podaj liczbę całkowitą: "))
divisor_parity = input("Podaj parzystość dzielników (even/odd): ")

if divisor_parity.lower() in ["even", "odd"]:
    result = count_divisors(integer_input, divisor_parity.lower())
    print(f"Liczba {divisor_parity} dzielników liczby {integer_input} wynosi: {result}")
else:
    print("Podaj poprawną parzystość dzielników (even/odd).")