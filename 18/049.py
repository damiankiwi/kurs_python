a, b, c = map(int, input("Podaj długości dwóch przylegających boków i przekątnej równoległoboku (oddzielone przecinkami): ").split(','))

if a**2 + b**2 == c**2:
    print("To jest prostokąt.")
elif a == b and b == c:
    print("To jest romb.")
else:
    print("To nie jest ani prostokąt, ani romb.")