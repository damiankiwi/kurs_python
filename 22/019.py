import itertools

def fizzbuzz(n):
    fizz = itertools.cycle(['', '', 'Fizz'])
    buzz = itertools.cycle(['', '', '', '', 'Buzz'])

    for i in range(1, n + 1):
        fizz_str = next(fizz)
        buzz_str = next(buzz)
        if fizz_str or buzz_str:
            print(f'{fizz_str}{buzz_str}')
        else:
            print(i)

fizzbuzz(15)