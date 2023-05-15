#2.  Nie korzystając z funkcji wbudowanej min(),
# napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).


def min_of(val1, val2):
    return val1 if val1 < val2 else val2
def minimum_of(a, b, c):
    tmp = min_of(a, b)
    return min_of(c, tmp)

def main():
    # ---- glowny kod
    x, y, z = [7, 15, 3]
    result = minimum_of(x, y, z)
    print(result)

main()