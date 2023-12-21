def liczba_argumentow(*args):
    return len(args)


print(liczba_argumentow())
print(liczba_argumentow(1))
print(liczba_argumentow(1, 2))
print(liczba_argumentow(1, 2, 3))
print(liczba_argumentow(1, 2, 3, 4))
print(liczba_argumentow([1, 2, 3, 4]))