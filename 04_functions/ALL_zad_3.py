# 3. 3▹ Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2  #operator trój argumentowy
    # if val1 > val2:
    #     return val1
    # else:
    #     return val2

def maximum_of(a, b, c):
    tmp = ''
    tmp = max_of_two(a, b)
    # if a > b:
    #     tmp = a
    # else:
    #     tmp = b
    return max_of_two(c, tmp)
    # if c > tmp:
    #     return c
    # else:
    #     return tmp

def main():
    x, y, z = [15, 13, 2]
    result = maximum_of(x, y, z)
    print(result)

main()
# if a > b or a > c:
#     print('A jest najwieksza liczba')
# if b > c:
#     print('B jest najwieksza lista')
# else:
#     print('C jest najwieksza liczba i wynosi: ', c)

# if a > b:
#     tmp = a
# else:
#     tmp = b
#
# if c > tmp:
#     print('Największa wartośćto', c)
# else:
#     print('Największa wartośćto', tmp)
