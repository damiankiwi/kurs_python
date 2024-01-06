def czy_wzglednie_pierwsze(a, b):
    def znajdz_najwiekszy_wspolny_dzielnik(x, y):
        while y:
            x, y = y, x % y
        return x

    return znajdz_najwiekszy_wspolny_dzielnik(a, b) == 1

print(czy_wzglednie_pierwsze(17, 13))
print(czy_wzglednie_pierwsze(17, 21))
print(czy_wzglednie_pierwsze(15, 21))
print(czy_wzglednie_pierwsze(25, 45))