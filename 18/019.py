def find_n_for_degrees_of_2():
    n = 1
    while True:
        number_str = '2' * n
        number = int(number_str)
        if number == 2 ** n:
            return n
        n += 1

result = find_n_for_degrees_of_2()
print(f'Wartość n to {result}')
